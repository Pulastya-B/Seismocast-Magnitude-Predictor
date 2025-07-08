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
  - Included in the `Scripts/` folder as `earthquake_dataset_extraction.py`
  - Data collected in safe 4-year chunks to avoid API limits

- **Basic EDA and Data Cleaning Completed**
  - Analyzed distributions of key features (`depth`, `mag`, `latitude`, `longitude`)
  - Identified and handled missing values, outliers, and inconsistencies
  - Parsed the `time` column into usable components like `year`, `month`, etc.
  - Notebook saved as: `data_preprocessing/data_cleaning.ipynb`

---

### 🛠️ Up Next

- **Feature Engineering**
  - Creating derived features like `elapsed_years`, `month_sin`, and spatial clusters (`cluster_id`)
  - Evaluating new features via correlation heatmaps and box plots against magnitude
  - Preparing cleaned dataset for model training

---

📁 Repo Structure (So Far)

