import streamlit as st
import plotly.express as px
from backend import get_data

# Add page title, title, texy input, slider, selectbox
st.set_page_config(page_title="Weather")
st.title("Weather Forecast for the Next couple Days!")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select date to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}

if place:
    try:
        # Get the temp/Sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky]
            st.image(image_paths, width=115)
    except KeyError:
        st.text(f"This city name {place} does not exist in this database.")