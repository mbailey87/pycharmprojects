from json import JSONDecodeError
import streamlit as st
import pandas as pd
import numpy as np
import cufflinks as cf
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from cufflinks.datagen import histogram
from scipy.stats import gaussian_kde
import requests, os, json

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("RENTCAST_API")
# #requset information
#
# zipcodes = ['84058', '84043', "84097", "84604", "84601"]
#
# for zipcode in zipcodes:
#
#     url = f"https://api.rentcast.io/v1/listings/sale?zipCode={zipcode}&status=Active&limit=50"
#
#     headers = {
#         "accept": "application/json",
#         "X-API-Key": api_key
#     }
#
#     response = requests.get(url, headers=headers)
#
#     if response.status_code == 200:
#         new_data = response.json()
#
#         try:
#             with open(f"data/rental_data_{zipcode}.json","w") as json_file:
#                 json.dump(new_data, json_file, indent=4)
#             print(f"Data successfully written for {zipcode}")
#
#         except requests.exceptions.RequestException as e:
#
#             print(f"Error during API request: {e}")
#
#
#         except json.JSONDecodeError as e:
#
#             print(f"Error decoding JSON response: {e}")
#     else:
#         print(f"Failed for {zipcode}: {response.status_code}")
st.set_page_config(
    layout="wide",
    page_title="Broker App",
    page_icon="🏠"
)

directory = "./data"
st.radio("How to search", ['Zipcode', 'City & State'])


if "Zipcode" in st.session_state:
    def find_data_zipcode(zipcode):
        file_name = f'data_{zipcode}.json'
        if file_name in os.listdir(directory):
            df = pd.read_json(f"./data/{file_name}")
            return df
        else:
            return None

    # --- User input
    zip_input = st.text_input('Zipcode', placeholder='enter a zipcode')

    # --- When user clicks submit
    if st.button("Submit") and zip_input:
        df = find_data_zipcode(zip_input)

        if df is not None:
            st.write(f"Zipcode {zip_input} Found!")
            st.dataframe(df)

            prices = df['price'].dropna()
            prices = prices[prices > 10000]

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
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=0.99
                ),
                bargap=0.2
            )

            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(sales_data, use_container_width=True)
            with col2:
                if 'latitude' in df.columns and 'longitude' in df.columns:
                    st.map(df[['latitude', 'longitude']])
                else:
                    st.write("Map data not available.")
        else:
            st.warning(f"Zipcode {zip_input} not found in ./data")

# df = pd.read_json(f'./data/data_{zip_input}.json')
# st.dataframe(df)
# sales_fig = px.histogram(df, x=df.price, nbins=40)
#
# price_bin = [price for price in df.price]
# st.write(price_bin)






