import streamlit as st
import pandas as pd

st.title("Car Price Prediction Dashboard")

year = st.number_input("Year", 2010, 2025, 2020)
mileage = st.number_input("Mileage", 0, 200000, 20000)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel"]
)

fuel_diesel = 1 if fuel == "Diesel" else 0

input_data = pd.DataFrame({
    "Year":[year],
    "Mileage":[mileage],
    "FuelType_Petrol":[0],
    "FuelType_Diesel":[fuel_diesel]
})

if st.button("Predict Price"):
    price = model.predict(input_data)
    st.success(f"Predicted Price: ₹ {price[0]:,.0f}")
