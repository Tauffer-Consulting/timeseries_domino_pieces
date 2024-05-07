from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import pandas as pd
from prophet import Prophet
from prophet.serialize import model_to_json
import plotly.graph_objs as go


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



        return OutputModel(
            model_file_path=,
            results_figure_file_path=
        )