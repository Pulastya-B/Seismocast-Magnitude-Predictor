# SeismoCast Streamlit App (Google Colab compatible)
# ================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
from geopy.geocoders import Nominatim

# Load trained model
model = joblib.load("App/modelXGB2.pkl")

# Load dataset that contains cluster_id
try:
    df = pd.read_csv("App/df_streamlit.csv")
except FileNotFoundError:
    raise ValueError("df_streamlit.csv not found. Please ensure it's in your Colab environment.")

# ------------------------------
# Reverse Geolocation Helper
# ------------------------------
@st.cache_data(show_spinner=False)
def reverse_geocode(lat, lon):
    try:
        geolocator = Nominatim(user_agent="seismocast")
        location = geolocator.reverse((lat, lon), timeout=5)
        return location.address if location else "Unknown"
    except:
        return "Geocoding Failed"

# ------------------------------
# Streamlit Page Config + Theme
# ------------------------------
st.set_page_config(page_title="SeismoCast", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1607990281364-68e08b2abacc');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 SeismoCast")
st.subheader("Machine Learning-Based Earthquake Magnitude Estimation")

# ------------------------------
# Input Section with Calendar
# ------------------------------
st.markdown("### 🌍🫨🫨 Enter Earthquake Details")
col1, col2 = st.columns(2)

with col1:
    lat = st.number_input("Latitude", value=27.7)
    
    depth = st.number_input("Depth (km)", value=1.0)

with col2:
    lon = st.number_input("Longitude", value=85.3)
    date = st.date_input("Select Date", value=datetime(2023, 1, 1),
                         min_value=datetime(1960, 1, 1), max_value=datetime(2040, 12, 31))
    year = date.year
    month = date.month
    day = date.day

# ------------------------------
# Predict Button
# ------------------------------
if st.button("🎯 Predict"):
    # Find the closest row to get cluster_id
    nearest_row = df.loc[((df["latitude"] - lat)**2 + (df["longitude"] - lon)**2).idxmin()]
    cluster_id = int(nearest_row["cluster_id"])

    # ✅ Get cluster activity from the reference df
    cluster_activity = df[df["cluster_id"] == cluster_id].shape[0]

    # ✅ Calculate other engineered features
    elapsed_years = year - 2000
    month_sin = np.sin(2 * np.pi * month / 12)
    month_cos = np.cos(2 * np.pi * month / 12)

    # ✅ Input DataFrame (MUST match training feature order)
    X = pd.DataFrame([[lat, lon, depth, cluster_id, elapsed_years, month_sin, month_cos, cluster_activity]],
                 columns=["latitude", "longitude", "depth", "cluster_id", "elapsed_years", "month_sin", "month_cos", "cluster_activity"])

    # ✅ Predict
    magnitude = model.predict(X)[0]
    uncertainty = 0.3

    # ✅ Show results
    st.success(f"🌋 Predicted Magnitude: {magnitude:.2f} ± {uncertainty}")
    st.info(f"📍 Location: {reverse_geocode(lat, lon)}")
    st.map(pd.DataFrame({"latitude": [lat], "longitude": [lon]}))

# ------------------------------
# Sample Input Button
# ------------------------------
if st.button("🧪 Try Sample Input"):
    st.session_state.update({
        "Latitude": 35.6895,
        "Longitude": 139.6917,
        "Depth": 15.0,
        "Date": datetime(2027, 8, 11)
    })
    st.rerun()

# ------------------------------
# Earthquake Timeline Slider
# ------------------------------
st.markdown("### 📅 Earthquake Map by Year")

# Select year from available data
available_years = sorted(df["year"].dropna().unique().astype(int))
selected_year = st.slider("Select Year", min_value=min(available_years),
                          max_value=max(available_years), value=2010)

# Filter and show top earthquakes of that year
year_df = df[df["year"] == selected_year]
year_df = year_df.nlargest(100, "mag")  # Top 100 quakes by magnitude

if not year_df.empty:
    st.map(year_df[["latitude", "longitude"]])
    st.info(f"Showing top 100 earthquakes from {selected_year}")
else:
    st.warning(f"No data available for {selected_year}")

# ------------------------------
# Disclaimer
# ------------------------------
st.markdown("---")
st.markdown("""
> ⚠️ **Disclaimer**: SeismoCast is a simulation tool trained on historical earthquake data.  
> It does **not predict future earthquakes**, but estimates likely magnitudes based on known spatial & depth conditions.  
> Ideal for awareness, educational use, and planning — not for emergency response or forecasting.
""")

st.caption("SeismoCast | Built with ❤️ by TechRx")
