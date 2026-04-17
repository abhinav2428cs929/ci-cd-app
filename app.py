import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# App Title
st.title("Breast Cancer Prediction App")

st.write("Enter the values to predict whether tumor is malignant or benign")

# Input sliders for some features
radius_mean = st.slider("Radius Mean", float(X.radius_mean.min()), float(X.radius_mean.max()))
texture_mean = st.slider("Texture Mean", float(X.texture_mean.min()), float(X.texture_mean.max()))
perimeter_mean = st.slider("Perimeter Mean", float(X.perimeter_mean.min()), float(X.perimeter_mean.max()))
area_mean = st.slider("Area Mean", float(X.area_mean.min()), float(X.area_mean.max()))
smoothness_mean = st.slider("Smoothness Mean", float(X.smoothness_mean.min()), float(X.smoothness_mean.max()))

# Create input data
input_data = np.zeros((1, X.shape[1]))
input_data[0][0] = radius_mean
input_data[0][1] = texture_mean
input_data[0][2] = perimeter_mean
input_data[0][3] = area_mean
input_data[0][4] = smoothness_mean

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("Malignant (Cancerous)")
    else:
        st.success("Benign (Non-Cancerous)")