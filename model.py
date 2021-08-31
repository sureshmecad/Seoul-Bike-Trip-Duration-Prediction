import joblib
from lightgbm import LGBMRegressor
import os
import numpy as np


curr_path = os.path.dirname(os.path.realpath(__file__))
LGBM = joblib.load(curr_path + '/model.joblib')


def predict(attributes: np.array):
    
    pred = LGBM.predict(attributes)

    print("BIKE TRIP PRICE Predicted")

    return pred[0]