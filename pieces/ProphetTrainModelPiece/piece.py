from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import pandas as pd
from prophet import Prophet
import pickle
from pathlib import Path

class ProphetTrainModelPiece(BasePiece):
    """
    This Piece trains a Prophet model using the data provided in the input file.
    """
    def piece_function(self, input_data: InputModel):

        # Load data
        input_data_file = input_data.input_data_file
        if input_data_file.endswith('.csv'):
            df = pd.read_csv(input_data_file)
        elif input_data_file.endswith('.json'):
            df = pd.read_json(input_data_file)
        else:
            raise ValueError("File format not supported. Please pass a CSV or JSON file.")

        model = Prophet()
        model.fit(df)

        # Serialize model
        model_file_path = Path(self.results_path) / "prophet_model.json"
        with open(str(model_file_path), "wb") as f:
            pickle.dump(model, f)

        return OutputModel(
            prophet_model_file_path=str(model_file_path),
        )