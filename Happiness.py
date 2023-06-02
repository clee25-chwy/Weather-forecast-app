import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="Happiness",
)

st.title("In Search for Happiness")
select_list = ["GDP", "Happiness", "Generosity"]
option_1 = st.selectbox("Select data for x-axis", select_list, key="first")
option_2 = st.selectbox("Select data for y-axis", select_list, key="second" )

st.subheader(f"{option_1} and {option_2}")
def get_data(option_1, option_2):
    df = pd.read_csv("Happy.csv")
    return df[option_1.lower()], df[option_2.lower()]

o1, o2 = get_data(option_1, option_2)

figure = px.scatter(x=o1, y=o2, labels={"x": option_1, "y": option_2})
st.plotly_chart(figure)