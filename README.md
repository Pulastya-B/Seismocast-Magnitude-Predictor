# TechRx-Seismocast

# 🌍 SeismoCast: Earthquake Magnitude Estimation using Machine Learning

**SeismoCast** is a machine learning-based project to estimate earthquake magnitudes from spatial and temporal features like latitude, longitude, depth, and time. This project is being developed as part of a hackathon.

---

## 🚧 Project Progress

### ✅ What’s Done
- **Dataset Extraction Completed**
  - Fetched global earthquake data from the [USGS Earthquake Catalog](https://earthquake.usgs.gov/fdsnws/event/1/) using a custom script.
  - Time range covered: **2000 to June 2025**
  - Total records: **~175,948**
  - Saved as: `usgs_earthquake_data_2000_2025.csv`

- **Data Fetch Script**
  - Included in the `scripts/` folder as `usgs_data_fetcher.py`
  - Data collected in safe 4-year chunks to avoid API limits

### 🔍 Currently Working On
- **Exploratory Data Analysis (EDA)**
  - Analyzing feature distributions (`depth`, `mag`, `latitude`, etc.)
  - Checking for missing values, outliers, and anomalies
  - Parsing `time` for year/month extraction

---

## 📁 Repo Structure (So Far)
