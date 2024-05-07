from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import yfinance as yf
from pathlib import Path


class GetYahooFinanceDataPiece(BasePiece):
    """
    This Piece trains a Prophet model using the data provided in the input file.
    """
    def piece_function(self, input_data: InputModel):
        ticker = input_data.ticker
        start_date = input_data.start_date
        end_date = input_data.end_date

        df = yf.download(ticker, start=start_date, end=end_date)
        df.reset_index(inplace=True)

        df_path = Path(self.results_path) / f"{ticker}_data.csv"
        df.to_csv(df_path, index=False)

        return OutputModel(
            data_path=str(df_path)
        )