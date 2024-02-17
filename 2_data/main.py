import streamlit as st
import pandas as pd

df = pd.read_csv("csv_data/sample.csv", dtype="int")

st.dataframe(df) # preferable
st.write(df)
st.table(df) # To display a simple table without any filters

st.metric(label="Expense", value=900, delta=20, delta_color="normal")