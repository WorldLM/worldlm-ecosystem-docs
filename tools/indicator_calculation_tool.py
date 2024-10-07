# indicator_calculation_tool.py

from typing import Any, Type
from pydantic import BaseModel, Field
from crewai_tools import BaseTool
import logging
import pandas as pd
import ta

class IndicatorCalculationToolSchema(BaseModel):
    data: pd.DataFrame

    model_config = {
        "arbitrary_types_allowed": True
    }

class IndicatorCalculationTool(BaseTool):
    name: str = "Indicator Calculation Tool"
    description: str = "Calculate technical indicators from historical data."
    args_schema: Type[BaseModel] = IndicatorCalculationToolSchema

    def _run(self, data: pd.DataFrame) -> Any:
        """Calculate technical indicators."""
        try:
            data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=14).rsi()
            macd = ta.trend.MACD(data['Close'])
            data['MACD'] = macd.macd()
            data['MACD_Signal'] = macd.macd_signal()
            data['MACD_Diff'] = macd.macd_diff()
            bb = ta.volatility.BollingerBands(data['Close'], window=20, window_dev=2)
            data['Bollinger High'] = bb.bollinger_hband()
            data['Bollinger Low'] = bb.bollinger_lband()
            # Add more indicators as needed
            return data
        except Exception as e:
            logging.error(f"Error calculating indicators: {e}")
            return None