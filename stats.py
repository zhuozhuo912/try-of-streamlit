import streamlit as st
import pandas as pd

st.write("""
## Download statistics

### Line chart

""")

# select DATE_FORMAT(date, '%Y-%m-%d') as d, count(id) as count from posts group by d;

dictionary = {'2020-06-25':34, '2020-06-26': 39, '2020-06-27': 40, '2020-06-28': 40, '2020-06-29': 42, '2020-06-30': 36}

series = pd.Series(dictionary)

st.line_chart(series)

st.write("""

### Bar chart

""")

st.bar_chart(series)