import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAc6ctooYBucHy1dvONh6IPPRqBX4U4H68")
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("⚡💧 Electricity & Water Usage Advisor")
st.write("Get personalized advice to save energy and water — and reduce your bills and environmental impact! 💚")

# Inputs
electricity_usage = st.number_input("Approximate monthly electricity usage (kWh)", min_value=0.0, value=200.0)
water_usage = st.number_input("Approximate monthly water usage (liters)", min_value=0.0, value=5000.0)
habits = st.text_area("Describe your habits (optional)", placeholder="e.g., I use air conditioning all day, take long showers...")

if st.button("Get Advice"):
    prompt = f"""
You are a helpful sustainability advisor. Based on the following inputs, suggest personalized energy and water-saving tips:

- Monthly electricity usage: {electricity_usage} kWh
- Monthly water usage: {water_usage} liters
- User habits: {habits}

Provide practical, easy-to-implement suggestions, and motivate the user to adopt them. Also mention potential estimated savings or environmental impact if possible.
"""

    response = model.generate_content(prompt)
    st.subheader("💡 Personalized Advice")
    st.write(response.text)
