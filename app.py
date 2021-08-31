import streamlit as st
from streamlit.proto.NumberInput_pb2 import NumberInput
from model import predict
import joblib
import os
import numpy as np

st.set_page_config(page_title="ADROIT",
                   page_icon="📵", layout="wide")

curr_path = os.path.dirname(os.path.realpath(__file__))


feature_cols = joblib.load(curr_path + "/features.joblib")

with st.form("prediction_form"):
    st.header("Enter the Details about App")

    Rating = st.number_input("Rating of APP: ")
    NumberofRatings = st.number_input("Total Ratings: ", value=0, format="%d")
    Price = st.number_input("App Price: ")
    Safe = st.number_input("Number of safe permissions: ", value=0, format="%d")
    Dangerous = st.number_input("Number of Dangerous permissions:", value=0, format="%d")
    permission = st.multiselect("Permit the app:",
                                feature_cols[5:35]) 
    Category = st.selectbox("Permit the app:",
                                feature_cols[35:])
    submit_val = st.form_submit_button("Predict Malware")



if submit_val:
    per_d = dict(zip(feature_cols[5:35],np.zeros(30)))
    for p in permission:
        per_d[p] = 1
    permission = np.array(list(per_d.values()))
    cat = dict(zip(feature_cols[35:], np.zeros(15)))
    cat[Category] = 1
    Category = np.array(list(cat.values()))

    base_feats = np.array([Rating, NumberofRatings, Price, Dangerous, Safe])

    attributes = np.concatenate([base_feats, permission, Category])
    
    print("attributes value")

    status = predict(attributes.reshape(1, -1))

    if status:
        st.error("The App is Malware")
    else:
        st.success("The App is Benign")
        st.balloons()