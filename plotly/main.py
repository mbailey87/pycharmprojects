import streamlit as st
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.offline as pyo
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

# # Setup for offline plotting
# cf.go_offline()
# cf.set_config_file(offline=True)
#
# # Create DataFrame
# arr_1 = np.random.randn(50, 4)
# df_1 = pd.DataFrame(arr_1, columns=['A', 'B', 'C', 'D'])
#
# # Generate interactive plot and open in browser
# fig = df_1.iplot(asFigure=True)  # Create the figure object
# pyo.plot(fig, filename='plot.html')  # Save and open in browser

# arr_1 = np.random.randn(50, 4)
# df_1 = pd.DataFrame(arr_1, columns=['A', 'B', 'C', 'D'])
#
# fig = px.line(df_1)
# fig.write_html('plot.html', auto_open=True)

# lineplots
df_stocks = px.data.stocks()
# fig = px.line(df_stocks, x='Date', y="GOOG", labels={'x': "Date", 'y': "Price"})

# fig = px.line(df_stocks, x="date", y=['GOOG', "AAPL"], labels={'x': "Date", 'y': "Price"}, title="Apple vs Google")
# fig.write_html('plot.html', auto_open=True)

pio.renderers.default = 'browser'   # Force Plotly to open in your web browser
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AAPL, mode='lines', name="Apple"))
line_fig.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AMZN, mode='lines+markers', name="Amazon"))
line_fig.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.GOOG, mode='lines+markers', name="Google", line=dict(color='firebrick', width=2, dash='dashdot')))

# line_fig.update_layout(title="Stock price data 2018 to 2020", xaxis_title='Price', yaxis_title="Date")

line_fig.update_layout(xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204,204,204)', linewidth=2, ticks="outside", tickfont=dict(family='Arial', size=14, color="rgb(82,82,82)")), yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False), autosize=False, margin=dict(autoexpand=False, l=100, r=20, t=110), showlegend=False, plot_bgcolor='black')

event = st.plotly_chart(line_fig)


