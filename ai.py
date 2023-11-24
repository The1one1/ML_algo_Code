import streamlit as st
import pandas as pd
import json
import io
import time
import psutil

@st.cache_data  # This function will be cached
def load_data(uploaded_file):
    # Read the contents of the uploaded file
    data = uploaded_file.read().decode()

    # Convert the JSON data into a DataFrame
    df = pd.read_json(io.StringIO(data), lines=True)

    return df

# Ask the user to upload a file
uploaded_file = st.file_uploader("Upload a JSON file")

if uploaded_file is not None:
    start_time = time.time()
    df = load_data(uploaded_file)
    execution_time = time.time() - start_time

    # Add a slider to select how many rows to display
    rows = st.slider('Number of rows to display', min_value=10, max_value=len(df))

    # Display the selected number of rows from the DataFrame as a table in Streamlit
    st.table(df.head(rows))

    # Print the execution time and RAM usage
    st.write(f"Execution time: {execution_time} seconds")
    st.write(f"RAM usage: {psutil.Process().memory_info().rss / 1024 ** 2} MB")