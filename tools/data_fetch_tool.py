# data_fetch_tool.py

import os
from typing import Any, Type, Optional
from pydantic import BaseModel, Field
from crewai_tools import BaseTool
from binance.client import Client
import pandas as pd
from datetime import datetime
import logging

class DataFetchToolSchema(BaseModel):
    symbol: str = Field(..., description="Trading pair symbol, e.g., 'BTCUSDT'")
    interval: str = Field(..., description="Time interval, e.g., '1h', '4h', '1d'")

class DataFetchTool(BaseTool):
    name: str = "Data Fetch Tool"
    description: str = "Fetch historical trading data for a given symbol and interval."
    args_schema: Type[BaseModel] = DataFetchToolSchema

    def __init__(self, api_key: Optional[str] = None, secret_key: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key or os.getenv('API_KEY')
        self.secret_key = secret_key or os.getenv('SECRET_KEY')
        self.client = Client(self.api_key, self.secret_key)

    def _run(self, symbol: str, interval: str) -> Any:
        """Fetch historical data for the given symbol and interval."""
        try:
            klines = self.client.get_historical_klines(
                symbol=symbol,
                interval=interval,
                start_str="1 Jan 2020",
                end_str=datetime.utcnow().strftime('%d %b %Y')
            )
            df = pd.DataFrame(klines, columns=[
                'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
                'Close Time', 'Quote Asset Volume', 'Number of Trades',
                'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'
            ])
            # Process and clean data as needed
            return df
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            return None