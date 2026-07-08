import streamlit as st
import requests

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter house details below to predict the selling price.")

overall_qual = st.number_input("Overall Quality", min_value=1.0, max_value=10.0, value=5.0)

gr_liv_area = st.number_input("Ground Living Area (sq ft)", value=1500.0)

garage_cars = st.number_input("Garage Cars", value=2.0)

garage_area = st.number_input("Garage Area", value=500.0)

total_bsmt = st.number_input("Total Basement Area", value=800.0)

first_flr = st.number_input("1st Floor Area", value=900.0)

full_bath = st.number_input("Full Bathrooms", value=2.0)

total_rooms = st.number_input("Total Rooms Above Ground", value=6.0)

year_built = st.number_input("Year Built", value=2005.0)

year_remod = st.number_input("Year Remodeled", value=2008.0)


if st.button("Predict House Price"):

    data = {
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "GarageArea": garage_area,
        "TotalBsmtSF": total_bsmt,
        "FirstFlrSF": first_flr,
        "FullBath": full_bath,
        "TotRmsAbvGrd": total_rooms,
        "YearBuilt": year_built,
        "YearRemodAdd": year_remod
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        prediction = response.json()

        st.success(
            f"Predicted House Price: ${prediction['Predicted House Price']:,.2f}"
        )

    except Exception as e:

        st.error("Could not connect to FastAPI backend.")

        st.write(e)