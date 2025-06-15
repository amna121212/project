import streamlit as st
from model_loader import ModelLoader
from predictor import Predictor
from preprocessor import Preprocessor

# Title
st.set_page_config(page_title="Success Probability Prediction", layout="centered")
st.title("📊 Company Success Probability Predictor")

# Load Model
model_loader = ModelLoader("svm_model_largest_companies.pkl")  # Make sure this file is in same folder
model = model_loader.model

# Create Preprocessor and Predictor instances
preprocessor = Preprocessor()
predictor = Predictor(model)

# Input Fields
st.header("🔧 Enter Company Details:")

revenue = st.number_input("Revenue (in Millions USD)", min_value=0.0, step=0.1)
employees = st.number_input("Number of Employees", min_value=1, step=1)
market_cap = st.number_input("Market Cap (in Billions USD)", min_value=0.0, step=0.1)

sector = st.selectbox("Select Sector", preprocessor.sectors)
country = st.selectbox("Select Country", preprocessor.countries)

# Button
if st.button("Predict Success Probability"):
    sector_encoded = preprocessor.encode_sector(sector)
    country_encoded = preprocessor.encode_country(country)

    input_data = [revenue, employees, market_cap, sector_encoded, country_encoded]
    prediction = predictor.predict(input_data)

    

    st.success(f"✅ Predicted Success Probability: **{round(prediction * 100, 2)}%**")


