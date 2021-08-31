import joblib
from sklearn.ensemble import RandomForestClassifier
import os
import numpy as np


curr_path = os.path.dirname(os.path.realpath(__file__))
rf = joblib.load(curr_path + '/model.joblib')


def predict(attributes: np.array):
    
    pred = rf.predict(attributes)

    print("Malware Status Predicted")

    return pred[0]