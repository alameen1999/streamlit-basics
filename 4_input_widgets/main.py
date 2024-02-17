import streamlit as st
import pandas as pd

# Buttons
primary_btn = st.button(label='Primary', type='primary')
secondary_btn = st.button(label='secondary', type='secondary')

if primary_btn:
    st.write("Hello from primary")

if secondary_btn:
    st.write("Hello from secondary")

# Checkbox
st.divider()

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("Remember you")
else:
    st.write("Forget you")


# Radio Buttons
st.divider()

df = pd.read_csv("data/sample.csv")
radio = st.radio("Choose a Column", options=df.columns[1:], index=0, horizontal=False)
st.write(radio)

# SelectBox
st.divider()
selection = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(selection)

# Multiselect
st.divider()

multiselect = st.multiselect("Choose as many columns", options=df.columns[1:], max_selections=3)
st.write(multiselect)

# Slider
st.divider()

slider = st.slider('Pick a number', min_value=0, max_value=10, value=0, step=1)
st.write(slider)

# Text Input
st.divider()

text_input = st.text_input("What your name", placeholder="Al Ameen")
st.write(f"Your name is {text_input}")

# Number Input
st.divider()

number_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {number_input}")

# Text Area
st.divider()

text_area = st.text_area("What do you want to tell me", height=200, placeholder="Write your message here")
st.write(text_area)

