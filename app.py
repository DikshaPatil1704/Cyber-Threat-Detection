import streamlit as st
import tensorflow as tf
import numpy as np

# --------------------------
# APP TITLE
# --------------------------
st.set_page_config(page_title="Network Attack Detection", page_icon="🚨")
st.title("🚨 Network Attack Detection App")
st.write("Enter the feature values below to predict whether the network traffic is normal or an attack.")

# --------------------------
# LOAD MODEL
# --------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("cyber_mlp_model.keras")
    return model

model = load_model()

# --------------------------
# USER INPUT
# --------------------------
input_data = st.text_input("Enter comma-separated feature values (example: 0.1, 2.3, 1.5, 0.0, 3.2)")

# PREDICTION
if st.button("🔍 Predict"):
    try:
        # Convert string → numpy array
        input_data = np.array([list(map(float, input_data.split(',')))])

        # Check input length
        if input_data.shape[1] != 186:
            st.error(f"⚠ You must enter exactly 186 numeric values, but got {input_data.shape[1]}.")
        else:
            # Make prediction
            prediction = model.predict(input_data)
            result = 'Attack' if prediction[0][0] > 0.5 else 'Normal'
            st.success(f"✅ Prediction: {result}")

    except Exception as e:
        st.error(f"⚠ Error: Please enter valid numeric values.\n\nDetails: {e}")