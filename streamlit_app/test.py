import streamlit as st
import random, time
import pandas as pd
import numpy as np
from streamlit import columns

#
# ran_num = random.randrange(1,10)
# print(ran_num)
#
# st.title('Welcome to Number Guess')
# st.write("Guess a number between 1 and 10 ")
#
# txt_guess = int(st.text_input('enter a number between 1 and 10', 1))
#
# if txt_guess > ran_num:
#     st.write("to high")
# elif txt_guess < ran_num:
#     st.write('to low')
# else:
#     st.write('thats correct')

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40
#     ]})
#
# df ## Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using st.write()

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40
# ]}))
#
# dframe = np.random.randn(10,100)
# st.dataframe(dframe)

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
#
# # st.dataframe(dataframe.style.highlight_max(axis=0))
#
# st.table(dataframe)


## Map Data
# chart_data = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=["a","b", 'c']
# )
# st.line_chart(chart_data)
#
# map_data = pd.DataFrame(
#     np.random.randn(100,2) / [50,50] + [37.76, -122.4],
#     columns=['lat', 'lon']
# )
#
# st.map(map_data)

## widgets
# x=st.slider('x')
#
# st.write(x, 'squared is', x*x)
# #_________
#
# st.text_input('your name', key='name')
#
# st.session_state.name
#
# #_____________
# if st.checkbox("Show Dataframe"):
#     chart_data = pd.DataFrame(
#         np.random.randn(20,3),
#         columns=["A", "B", "C"]
#     )
#     chart_data
# #__________
# df = pd.DataFrame({
#     'first column': [1,2,3,4],
#     'second column': [10,20,30,40]
# })
#
# option = st.selectbox(
#     'Which number do you like best',
#     df['first column']
# )
#
# 'you selected: ', option

## Layout

# # add a selectbox to a sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', "Home Phone", "Cell Phone")
# )
#
# add_slider = st.sidebar.slider(
#     "select range of values",
#     0.0,100.0,(25.0, 75.0)
# )
#
# left_column, center_column, right_column = st.columns(3)
# # you can use a column like st.sidebar
# left_column.button('Press Me!')
#
# center_column.button('No Press ME!')
# # you can call Streamlit functions inside a "with" block:
# with right_column:
#     chosen= st.radio(
#         "Sorting hat",
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
#     )
#     st.write(f'Your in {chosen} house!')

## Show Progress
# "starting a long computation"
# latest_iteration = st.empty() # placeholder
# bar=st.progress(0)
#
# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)
#
# "...and now we're done"

## Cashing
# '''
# @st.cache_data
# def long_running_function(param1, param2):
#     return …
# In the above example, long_running_function is decorated with @st.cache_data. As a result, Streamlit notes the following:
#
#     The name of the function ("long_running_function")
#     The value of the inputs (param1, param2)
#     The code within the function
#
# Before running the code within long_running_function, Streamlit checks its cache for a previously saved result.
# If it finds a cached result for the given function and input values, it will return that cached result and not rerun function's code.
# Otherwise, Streamlit executes the function, saves the result in its cache, and proceeds with the script run.
# During development, the cache updates automatically as the function code changes, ensuring that the latest changes are reflected in the cache.
# '''

# Session State

# if "counter" not in st.session_state:
#     st.session_state.counter = 0
#
# st.session_state.counter += 1
#
# st.header(f"This page has run {st.session_state.counter} times")
# st.button("Run it again")

# '''
# Session State provides a dictionary-like interface where you can save information that is preserved between script reruns.
# Use st.session_state with key or attribute notation to store and recall values.
# For example, st.session_state["my_key"] or st.session_state.my_key.
# Remember that widgets handle their statefulness all by themselves, so you won't always need to use Session State!
#
# First run: The first time the app runs for each user, Session State is empty. Therefore, a key-value pair is created ("counter":0).
# As the script continues, the counter is immediately incremented ("counter":1) and the result is displayed: "This page has run 1 times."
# When the page has fully rendered, the script has finished and the Streamlit server waits for the user to do something. When that user clicks the button, a rerun begins.
#
# Second run: Since "counter" is already a key in Session State, it is not reinitialized. As the script continues, the counter is incremented ("counter":2) and the result is displayed: "This page has run 2 times."
#
# There are a few common scenarios where Session State is helpful.
# As demonstrated above, Session State is used when you have a progressive process that you want to build upon from one rerun to the next.
# Session State can also be used to prevent recalculation, similar to caching. However, the differences are important:
#
# Caching associates stored values to specific functions and inputs. Cached values are accessible to all users across all sessions.
# Session State associates stored values to keys (strings). Values in session state are only available in the single session where it was saved.
# If you have random number generation in your app, you'd likely use Session State. Here's an example where data is generated randomly at the beginning of each session.
# By saving this random information in Session State, each user gets different random data when they open the app but it won't keep changing on them as they interact with it.
# If you select different colors with the picker you'll see that the data does not get re-randomized with each rerun.
# (If you open the app in a new tab to start a new session, you'll see different data!)
#
#
# '''

# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
#
# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)