# market_analysis_tool.py

from typing import Any, Type
from pydantic import BaseModel, Field, ConfigDict
from crewai_tools import BaseTool
from typing import Optional
import pandas as pd
import os
import openai
import logging

class MarketAnalysisToolSchema(BaseModel):
    data: pd.DataFrame = Field(..., description="Data with technical indicators")
    symbol: str = Field(..., description="Trading pair symbol, e.g., 'BTCUSDT'")
    interval: str = Field(..., description="Time interval, e.g., '1h', '4h', '1d'")
    model_config = ConfigDict(arbitrary_types_allowed=True)


class MarketAnalysisTool(BaseTool):
    name: str = "Market Analysis Tool"
    description: str = "Analyze market data using OpenAI's GPT models."
    args_schema: Type[BaseModel] = MarketAnalysisToolSchema

    def __init__(self, openai_api_key: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.openai_api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        openai.api_key = self.openai_api_key

    def _run(self, data: pd.DataFrame, symbol: str, interval: str) -> Any:
        """Perform market analysis using OpenAI API."""
        try:
            prompt = f"""
You are an expert financial market analyst with unparalleled knowledge and a deep understanding of cryptocurrency markets. You have access to the latest technical indicators for the {symbol} trading pair.

For the large timeframe ({interval}), the following technical indicators have been calculated:

{data.tail().to_string(index=False)}

Please provide a comprehensive and insightful analysis based on the above data. Focus on:
1. How the large timeframe indicators suggest potential market movement.
2. Highlight any significant patterns emerging that could impact the market trend.

Ensure that your response is clear, professional, and includes detailed market insights without making direct investment recommendations.
"""
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            logging.error(f"Error in market analysis: {e}")
            return None