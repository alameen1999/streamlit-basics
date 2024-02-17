import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csv_data/sample.csv")
st.dataframe(df)
# Streamlit line plot
st.line_chart(df, x="year", y=["col1", "col2", "col3"])

# Streamlit area chart
st.area_chart(df, x="year", y=["col1", "col2", "col3"])

# Streamlit bar chart
st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# Streamlit map
geo_df = pd.read_csv("csv_data/sample_map.csv")
st.dataframe(geo_df)
st.map(geo_df)

# Matplotlib (To get more controls over figure use matplotlib or plotly)
fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title('My figure')
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate()
st.pyplot(fig)
