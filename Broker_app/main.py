import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy.stats import gaussian_kde

st.set_page_config(layout="wide", page_title="Broker App Prototype", page_icon="🏡")
st.title("🏡 MLS Market Data Viewer")

# --- Load all JSON files into memory ---
data_files = {
    "Orem": "./data/sales_data_Orem_UT.json",
    "Lehi": "./data/sales_data_Lehi_UT.json",
    "Draper": "./data/sales_data_Draper_UT.json",
    "Springville": "./data/rental_data_Springville_UT.json",
    "Saint George": "./data/rental_data_Saint_George_UT.json",
    "Ogden": "./data/rental_data_Ogden_UT.json",
    "Zip 84601": "./data/data_84601.json",
    "Zip 84043": "./data/data_84043.json",
    "Zip 84058": "./data/data_84058.json",
    "Zip 84097": "./data/data_84097.json",
}

@st.cache_data
def load_data():
    combined_data = []
    for city, file_path in data_files.items():
        if os.path.exists(file_path):
            with open(file_path) as f:
                raw = json.load(f)
                for r in raw:
                    r["source"] = city
                    if "rental" in file_path:
                        r["listingCategory"] = "Rental"
                    elif "sales" in file_path or "data_84" in file_path:
                        r["listingCategory"] = "Sales"
                    else:
                        r["listingCategory"] = "Unknown"
                combined_data.extend(raw)
    return pd.DataFrame(combined_data)

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Listings")
category_filter = st.sidebar.radio("Listing Category", ["All", "Sales", "Rental"])
search_mode = st.sidebar.radio("Search by", ["City & State", "Zipcode"])

if category_filter != "All":
    df = df[df["listingCategory"] == category_filter]

if search_mode == "City & State":
    city_options = sorted(df["city"].dropna().unique())
    city_choice = st.sidebar.selectbox("Select City", city_options)
    filtered = df[df["city"] == city_choice]
else:
    zip_options = sorted(df["zipCode"].dropna().unique())
    zip_choice = st.sidebar.selectbox("Select Zipcode", zip_options)
    filtered = df[df["zipCode"] == zip_choice]

property_types = sorted(filtered["propertyType"].dropna().unique())
selected_types = st.sidebar.multiselect("Property Type", property_types, default=property_types)
filtered = filtered[filtered["propertyType"].isin(selected_types)]

min_beds = st.sidebar.number_input("Min Bedrooms", min_value=0, max_value=10, value=0)
max_beds = st.sidebar.number_input("Max Bedrooms", min_value=0, max_value=10, value=10)
max_price = st.sidebar.number_input("Max Price", min_value=10000, step=50000, value=2000000)
built_after = st.sidebar.number_input("Built After Year", min_value=1800, max_value=2100, value=1900)

if "bedrooms" in filtered.columns:
    filtered = filtered[(filtered["bedrooms"] >= min_beds) & (filtered["bedrooms"] <= max_beds)]
filtered = filtered[filtered["price"] <= max_price]
if "yearBuilt" in filtered.columns:
    filtered = filtered[filtered["yearBuilt"] >= built_after]

# --- Add Price per Sqft Column ---
filtered = filtered.copy()
filtered["pricePerSqft"] = (filtered["price"] / filtered["squareFootage"]).round(2)

# --- Display Listings ---
title_label = city_choice if search_mode == "City & State" else zip_choice
st.subheader(f"Listings in {title_label} ({category_filter})")
st.write(f"Showing {len(filtered)} properties")
st.dataframe(filtered[["formattedAddress", "propertyType", "price", "bedrooms", "bathrooms", "squareFootage", "pricePerSqft", "yearBuilt", "listingCategory"]].fillna("N/A"))

# --- Price Distribution Chart with KDE Line ---
st.subheader("📊 Price Distribution & Trend")
if not filtered.empty:
    prices = filtered["price"].dropna()
    if len(prices) > 1:
        kde_func = gaussian_kde(prices)
        x_values = np.linspace(prices.min(), prices.max(), 200)
        y_values = kde_func(x_values)

        sales_data = make_subplots(specs=[[{"secondary_y": True}]])

        sales_data.add_trace(go.Histogram(
            x=prices,
            nbinsx=40,
            name="Homes per Price Range"
        ), secondary_y=False)

        sales_data.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            name="Estimated Price Trend",
            mode='lines+markers',
            marker=dict(size=4)
        ), secondary_y=True)

        sales_data.update_layout(
            title_text=f"Price Distribution in {title_label}",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=0.99
            ),
            bargap=0.2
        )

        st.plotly_chart(sales_data, use_container_width=True)
    else:
        st.info("Not enough price data to generate a trend line.")
else:
    st.warning("No listings match your filter.")
