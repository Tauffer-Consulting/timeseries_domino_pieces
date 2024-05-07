from pydantic import BaseModel, Field
from enum import Enum
from typing import List
from datetime import date


class InputModel(BaseModel):
    model_path: str = Field(
        title="Model Path",
        description="Path to the file containing the trained model."
    )
    periods: int = Field(
        title="Periods",
        description="Number of periods to forecast."
    )


class OutputModel(BaseModel):
    forecast_data_path: str = Field(
        title="Forecast Data Path",
        description="Path to the file containing the forecast data."
    )
    forecast_figure_path: str = Field(
        title="Forecast Figure Path",
        description="Path to the file containing the results figure."
    )
