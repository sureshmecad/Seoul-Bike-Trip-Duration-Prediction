import streamlit as st
from streamlit.proto.NumberInput_pb2 import NumberInput
from model import predict
import joblib
import os
import numpy as np

st.set_page_config(page_title="SEOUL BIKE PRICE PREDICTION",
                   page_icon="📵", layout="wide")

curr_path = os.path.dirname(os.path.realpath(__file__))


feature_cols = joblib.load(curr_path + "/features.joblib")

with st.form("prediction_form"):
    st.header("Enter the Details about App")

    Distance = st.number_input("Distance: ")
    PLong = st.number_input("PLong: ")
    DLong = st.number_input("DLong: ")
    Haversine = st.number_input("Haversine: ")
    Pmonth = st.number_input("Pmonth:")
    Phour = st.number_input("Phour:") 
    PDweek = st.number_input("PDweek:")
    Dmonth = st.number_input("Dmonth")
    Dhour = st.number_input("Dhour")
    DDweek = st.number_input("DDweek")
    Temp = st.number_input("Temp")
    Wind = st.number_input("Wind")
    Humid = st.number_input("Humid")
    Solar = st.number_input("Solar")
    GroundTemp = st.number_input("GroundTemp")
    submit_val = st.form_submit_button("PREDICT")


if submit_val:
    
    attributes = np.array([Distance, PLong, DLong, Haversine, Pmonth, Phour, PDweek, Dmonth, Dhour, DDweek, Temp, Wind, Humid, Solar, GroundTemp])

       
    print("attributes value")

    status = predict(attributes.reshape(1, -1))
    
    if status>0:
        st.success(f"The Distance is {status}")
        st.balloons()