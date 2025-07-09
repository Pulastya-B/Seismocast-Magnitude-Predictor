# 🌍 SeismoCast: Earthquake Magnitude Estimation using Machine Learning

**SeismoCast** is a machine learning-based simulation tool designed to estimate earthquake magnitudes using spatial and temporal features like latitude, longitude, depth, and time. This project is developed as part of a hackathon and demonstrates how machine learning can assist in seismic awareness and risk analysis.

---

## ✅ Project Progress

### 📥 Dataset Extraction
- Fetched global earthquake data from the **USGS Earthquake Catalog API**.
- Time range: **2000 to June 2025**
- Total records: **~175,948**
- Script: `earthquake_dataset_extraction.py`

---

### 📊 Data Preprocessing
- Cleaned and standardized dataset
- Parsed `time` column to extract `year`, `month`, and `day`
- Removed missing values and outliers
- File: `data_preprocessing/data_cleaning.ipynb`

---

### 🧠 Feature Engineering
- Engineered spatial-temporal features to improve model learning:
  - `elapsed_years` (time since 2000)
  - `month_sin`, `month_cos` (cyclical encoding)
  - `cluster_id` (spatial cluster identifier)
  - `cluster_activity` (regional seismic activity level)
- File: `feature_engineering/feature_creation_validation.ipynb`

---

### 📈 Model Training & Evaluation
- Used **XGBoost Regressor** with `n_estimators = 300`
- Applied GridSearchCV for basic hyperparameter tuning
- Final metrics:
  - **MAE**: ~0.266  
  - **MSE**: ~0.140  
  - **R²**: ~0.073
- Visualized feature importance
- File: `model_training/xgb_model_training.ipynb`
- Trained model: `modelXGB2.pkl`

---

### 💻 Streamlit App (Offline for now)
- Built an interactive app to:
  - Predict magnitude from user input (lat/lon/depth/date)
  - Perform reverse geolocation
  - Visualize earthquakes by year
- File: `seismocast_app_final.py`

---

## 🛠️ Up Next
- [ ] **Deploy on Streamlit Cloud**  
  *(App not live yet – deployment in progress)*
- [ ] Finalize requirements.txt and hosting config

---

## 📁 Repo Structure
<details>
<summary>Click to expand</summary>

<br>

```text
SeismoCast/
├── Data_Preprocessing/
│   └── data_cleaning_eda.ipynb                # Initial EDA and data cleaning
│
├── Feature_Engineering/
│   └── feature_creation_validation.ipynb      # Feature derivation and correlation validation
│
├── dataset/
│   └── usgs_earthquake_data_2000_2025.csv     # Fetched USGS dataset
│
├── scripts/
│   └── earthquake_dataset_extraction.py       # Script for USGS API data fetching
|
├── Model_Building/
│   └── Model_Training.py
│
└── README.md
</details> 
