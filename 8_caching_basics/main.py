import streamlit as st
import time
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Caching demonstration")

st.button('Test cache')

st.subheader("st.cache_data")

@st.cache_data
def cache_this_function():
    time.sleep(2)
    out = 'Hello Sasi'
    return out

out = cache_this_function()
st.write(out)


st.subheader("st.cache_resource")

@st.cache_resource
def create_simple_linear_regression():
    time.sleep(2)
    x = np.array([1,2,3,4,5,6,7]).reshape(-1,1)
    y = np.array([1,2,3,4,5,6,7])

    model = LinearRegression().fit(x,y)
    return model
lr = create_simple_linear_regression() 
x_pred = np.array([8]).reshape(-1,1)
pred = lr.predict(x_pred)

st.write(f"The prediction is {pred[0]}")