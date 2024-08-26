import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit input fields
Glucose = st.number_input('Glucose', min_value=0)
Pregnancies = st.number_input('Pregnancies', min_value=0)
BMI = st.number_input('BMI', min_value=0.0)

# Make sure to only predict when all inputs are provided
if st.button('Predict'):
    # Check if all inputs are valid
    if Glucose is not None and Pregnancies is not None and BMI is not None:
        input_features = [[Glucose, Pregnancies, BMI]]
        try:
            output = model.predict(input_features)
            st.write(f"Prediction: {output[0]}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please provide all input values.")
