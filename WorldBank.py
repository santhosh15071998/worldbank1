import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
st.title('World Bank Data - India')
India=pd.read_csv('World_Bank_India.csv')
st.write(India)
st.table('World_Bank_India.csv',skiprows=1)

