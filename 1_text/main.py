import streamlit as st

# Title
st.title("POC for streamssadlit")

# Header
st.header('Main Header')

# Sub header
st.subheader('Sub Header')

# Markdown
st.markdown("Markdown **text**")
st.markdown("# Header1")
st.markdown("## Header2")


# Caption
st.caption("This is caption")

# Code block
st.code("""import pandas as pd
pd.read('my_csc_file')
""")

# Preformated text
st.text("Hello world")

# Latex
st.latex('x=2^2')

# Divider
st.text("above")
st.divider()
st.text("below")

# st.write()
st.write('Some text')