import streamlit as st
import plotly.express as px
from backend import get_data


# Add Title, Text Input, Slider, Selectbox, Subheader
st.title("5 Day Weather Forecast")
place = st.text_input("City: ")
days = st.slider("Days", min_value=1, max_value=5,
	            help="Select the number of days")
option = st.selectbox("Select the data to view:",
	            ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
	# DECONSTRUCTING TUPLE OF get_data(), extracting two lists
	# Get the Temperature, Sky data
	filtered_data = get_data(place, days)


	if option == "Temperature":
		temperatures = [dict["main"]["temp"] for dict in filtered_data]
		temp_celsius = [((f - 32) * 5/9) / 10 for f in temperatures]
		dates = [dict["dt_txt"] for dict in filtered_data]
		# CREATE A TEMPERATURE PLOT CHART
		figure = px.line(x=dates, y=temp_celsius, labels={"x":"Date", "y":"Temperature (°C)"})
		st.plotly_chart(figure)

	if option == "Sky":
		images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", 
		        "Rain":"images/rain.png", "Snow":"images/snow.png"}
		sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
		image_path = [images[condition] for condition in sky_condition]
		st.image(image_path, width=115)
