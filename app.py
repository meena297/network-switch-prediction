import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("📶 Smart Network Switch Prediction")
st.write("Predict whether a network switch is required based on network conditions.")

# -------- INPUTS --------
signal_strength = st.slider(
    "Signal Strength (dBm)",
    min_value=-120,
    max_value=-50,
    value=-80
)

internet_speed = st.slider(
    "Internet Speed (Mbps)",
    min_value=0,
    max_value=100,
    value=20
)

battery_level = st.slider(
    "Battery Level (%)",
    min_value=0,
    max_value=100,
    value=50
)

location = st.selectbox(
    "Location Type",
    ["Urban", "Semi-Urban", "Rural"]
)

# Convert location to numeric
if location == "Urban":
    location_val = 0
elif location == "Semi-Urban":
    location_val = 1
else:
    location_val = 2

# -------- DISPLAY VALUES --------
st.subheader("📊 Current Network Conditions")
st.write(f"Signal Strength: {signal_strength} dBm")
st.write(f"Internet Speed: {internet_speed} Mbps")
st.write(f"Battery Level: {battery_level} %")
st.write(f"Location Type: {location}")

# -------- PREDICTION --------
if st.button("Predict Network Switch"):
    input_data = np.array([[signal_strength, internet_speed, battery_level, location_val]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Network Switch Recommended")
    else:
        st.info("📡 Stay on Current Network")
