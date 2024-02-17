import streamlit as st
import pandas as pd

# Sidebar
with st.sidebar:
    st.text("Hello")

# Columns
col1, col2, col3 = st.columns(3)

col1.write("This is col1")

slider = col2.slider("Choose a number", min_value=0, max_value=10)

col3.write(slider)

# Tabs
df = pd.read_csv("csv_data/sample.csv")

tab1, tab2 = st.tabs(["Line plot", "Bar Chart"])

with tab1:
    tab1.write("Line plot")
    st.line_chart(df, x='year', y=['col1', 'col2', 'col3'])

with tab2:
    tab2.write("Bar Chart")
    st.bar_chart(df, x='year', y=['col1', 'col2', 'col3'])

# Expander (Collapsible element)
with st.expander("Click to expand"):
    st.write("Hello Ameen")

# Container
with st.container():
    st.write("Inside container")
st.write("outside container")
    