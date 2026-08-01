import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Visualization Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.write(df.head())

    st.subheader("📊 Basic Info")
    st.write(df.describe())

    column = st.selectbox("Select column for visualization", df.columns)

    chart_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])

    if chart_type == "Bar Chart":
        fig, ax = plt.subplots()
        df[column].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Line Chart":
        fig, ax = plt.subplots()
        df[column].plot(kind='line', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots()
        df[column].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
        st.pyplot(fig)