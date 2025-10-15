import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("flood_model.pkl")

st.title("🌊 AI Flood Risk Predictor")
st.write("Predict flood risk based on area size and environmental data.")

area = st.number_input("Area in Km²", min_value=0.0, step=0.1)
layer = st.number_input("Layer Encoded (e.g. 0-5)", min_value=0, max_value=10)

if st.button("Predict Flood Risk"):
    result = model.predict(pd.DataFrame({'Area_Km2': [area], 'layer_encoded': [layer]}))
    st.success("🌧️ Flood likely!" if result[0] == 1 else "☀️ No flood risk detected.")
