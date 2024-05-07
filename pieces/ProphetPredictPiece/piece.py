from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import pandas as pd
from prophet import Prophet
import pickle
from pathlib import Path
from prophet.plot import plot_plotly, plot_components_plotly



class ProphetPredictPiece(BasePiece):
    """
    This Piece uses a trained Prophet model to make predictions on new data.
    """
    def piece_function(self, input_data: InputModel):

        with open(input_data.prophet_model_path, "rb") as f:
            model = pickle.load(f)

        future = model.make_future_dataframe(periods=input_data.periods)
        forecast = model.predict(future)

        self.results_path = Path(self.results_path)

        forecast_data_path = self.results_path / "forecast_data.csv"
        forecast.to_csv(forecast_data_path, index=False)

        forecast_figure_path = self.results_path / "forecast_figure.json"
        forecast_figure = plot_plotly(model, forecast)

        forecast_figure.write_json(str(forecast_figure_path))
        self.display_result = {
            "file_type": "plotly_json",
            "file_path": str(forecast_figure_path)
        }

        return OutputModel(
            forecast_data_path=str(forecast_data_path),
            forecast_figure_path=str(forecast_figure_path),    
        )