import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv('../data/dashboard_data.csv')

st.title("Interactive Sales Dashboard")

st.subheader("Dataset")
st.write(df)

# Show sales chart
st.subheader("Monthly Sales")
st.line_chart(df.set_index('Month')['Sales'])

# Show profit chart
st.subheader("Monthly Profit")
st.bar_chart(df.set_index('Month')['Profit'])

# Metrics
st.subheader("Key Insights")

st.write("Total Sales:", df['Sales'].sum())
st.write("Total Profit:", df['Profit'].sum())
st.write("Average Sales:", df['Sales'].mean())