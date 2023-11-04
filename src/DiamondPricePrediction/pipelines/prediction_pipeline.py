import os
import sys
import pandas as pd
from src.DiamondPricePrediction.exception import customexception
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path=os.path.join("artifacts", "processor.pk1")
            model_path = os.path.join("artifacts", "model.pk1")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            scaled_data = preprocessor.transform(features) 

            pred = model.predict(scaled_data)

            return pred

        except Exception as e:
            raise customexception(e, sys)