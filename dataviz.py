import streamlit as st
import pandas as pd
import numpy as np


st.write("### Movies Dataset")
df = pd.read_csv('movies.csv')
st.write(df.head())

st.write("\n### Bar Chart")
x = np.random.randint(5, 25, 10)
y = np.arange(0, 10)

st.bar_chart(pd.DataFrame(x, y))

st.write("\n### Line Chart")
st.line_chart(pd.DataFrame(x, y))