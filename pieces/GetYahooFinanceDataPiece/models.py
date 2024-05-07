from pydantic import BaseModel, Field
from datetime import date



class InputModel(BaseModel):
    ticker: str = Field(
        description="Ticker of the stock to get data from."
    ) # TODO change to ENUM ?
    start_date: date = Field(
        description="Start date of the data to get."
    )
    end_date: date = Field(
        description="End date of the data to get."
    )

class OutputModel(BaseModel):
    data_path: str = Field(
        description="Path to the file containing the trained model."
    )
