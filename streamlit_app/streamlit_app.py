# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.title("Real Estate Market Trends")

# Simulate API call
zip_code = st.text_input("Enter ZIP Code", "84604")
house_type = st.selectbox("Select House Type", ["All", "Single-Family", "Condo", "Townhome"])

# In production, you'd call your actual API
# response = requests.get(f"https://api.example.com/market?zip={zip_code}&type={house_type}")
# data = pd.DataFrame(response.json())

# Mock Data
data = pd.DataFrame({
    "date": pd.date_range("2023-01-01", periods=12, freq='M'),
    "price": [300000 + i*5000 for i in range(12)],
    "type": ["Single-Family"] * 12,
    "zip": [zip_code] * 12
})

# Filter data
if house_type != "All":
    data = data[data["type"] == house_type]

# Chart
fig = px.line(data, x="date", y="price", title=f"Home Price Trend in {zip_code}")
st.plotly_chart(fig)

# Show data table
st.subheader("Raw Data")
st.dataframe(data)
