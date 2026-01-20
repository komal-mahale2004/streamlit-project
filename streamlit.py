import streamlit as st
import pandas as pd
import numpy as np

st.title("Missing Value Handling App")

st.write("This app shows how to handle missing values in data")

data = {
    "Age": [25, None, 30, 28],
    "Salary": [50000, 60000, None, 45000]
}

df = pd.DataFrame(data)

st.subheader("Original Data")
st.dataframe(df)

st.subheader("After Filling Missing Values")
st.dataframe(df.fillna(0))
