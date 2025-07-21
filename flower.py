import streamlit as st
import joblib
from sklearn.datasets import load_iris

iris = load_iris()

st.title("Iris Flower Classifier")
sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, format="%.2f")
sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, format="%.2f")
petal_length = st.number_input("Petal length (cm)", min_value=0.0, format="%.2f")
petal_width = st.number_input("Petal width (cm)", min_value=0.0, format="%.2f")

if st.button("Predict Flower"):
    try:
        model = joblib.load('model/iris_knn_model.joblib')
        sample = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(sample)[0]
        flower_name = iris.target_names[prediction]

        st.success(f"Predicted Flower: **{flower_name}** 🌼")
        
    except FileNotFoundError:
        st.error("Model file not found. Please run train_model.py first.")
