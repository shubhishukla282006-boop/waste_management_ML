import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.title("Waste Management Cost Prediction")

# Load dataset
df = pd.read_csv("Waste_Management_with_Extra_Features.csv")
st.write("Dataset Preview:", df.head())

# User input
recycling_rate = st.slider("Recycling Rate (%)", 0, 100, 50)
green_tech = st.slider("Green Tech Adoption", 0.0, 10.0, 5.0)

# Simple demo prediction (replace with trained model)
cost = 2000 + recycling_rate*10 - green_tech*50
st.write("Predicted Cost of Waste Management (₹/ton):", cost)
