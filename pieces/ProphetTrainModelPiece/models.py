from pydantic import BaseModel, Field
from enum import Enum
from typing import List
from datetime import date


class GrowthTrend(str, Enum):
    linear = "linear"
    logistic = "logistic"
    flat = "flat"


class SeasonalityMode(str, Enum):
    additive = "additive"
    multiplicative = "multiplicative"


class InputModel(BaseModel):
    input_data_file: str = Field(
        description="Path to the input data file. Accepted formats: `.csv`, `.json`."
    )
    datetime_column_name: str = Field(
        description="Name of the column containing the datetime values."
    )
    target_column_name: str = Field(
        description="Name of the column containing the target values."
    )
    test_set_percentage: float = Field(
        default=20.0,
        ge=1,
        le=90,
        description="Percentage of the data to use as test set. Default is 20%."
    )
    growth_trend: GrowthTrend = Field(
        default=GrowthTrend.linear,
        description="The growth trend of the data. Options are `linear`, `logistic` and `flat`. Default is `linear`."
    )
    changepoints: List[date] = Field(
        default=[],
        description="List of dates at which to include potential changepoints. If not specified, potential changepoints are selected automatically."
    )
    n_changepoints: int = Field(
        default=25,
        ge=0,
        le=1000,
        description=" Number of potential changepoints to include. Not used if input `changepoints` is supplied."
    )
    seasonality_mode: SeasonalityMode = Field(
        default=SeasonalityMode.additive,
        description="The seasonality mode of the data. Options are `additive` and `multiplicative`. Default is `additive`."
    )


class OutputModel(BaseModel):
    model_file_path: str = Field(
        description="Path to the file containing the trained model."
    )
    results_figure_file_path: str = Field(
        description="Path to the file containing the results figure."
    )
