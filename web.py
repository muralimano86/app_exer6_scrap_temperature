import streamlit as st
import plotly.express as px
import pandas as pd

st.header("Temp chart")

df = pd.read_csv("data.txt")
fig = px.line(x=df["date"], y=df["temperature"], labels={"x": "Date", "y": "Temp"})

st.plotly_chart(fig)