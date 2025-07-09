# TechRx-Seismocast

# 🌍 SeismoCast: Earthquake Magnitude Estimation using Machine Learning

**SeismoCast** is a machine learning-based project to estimate earthquake magnitudes from spatial and temporal features like latitude, longitude, depth, and time. This project is being developed as part of a hackathon.

---

## 🚧 Project Progress

### ✅ Dataset Extraction Completed
- Fetched global earthquake data from the **USGS Earthquake Catalog** using a custom script
- Time range covered: **2000 to June 2025**
- Total records: **~175,948**
- Saved as: `dataset/usgs_earthquake_data_2000_2025.csv`
- Script used: `scripts/earthquake_dataset_extraction.py`
- Data collected in **safe 4-year chunks** to avoid API rate limits

---

### ✅ Basic EDA and Data Cleaning Completed
- Analyzed distributions of key features (`depth`, `mag`, `latitude`, `longitude`)
- Handled missing values, outliers, and inconsistencies
- Parsed `time` into separate columns like `year`, `month`, and `day`
- Notebook saved as: `Data_Preprocessing/data_cleaning_eda.ipynb`

---

### ✅ Feature Engineering Completed
- Created derived features:
  - `elapsed_years`: Time since start of dataset
  - `month_sin` & `month_cos`: Cyclical encoding of month
  - `cluster_id`: Seismic region clusters via KMeans
  - `cluster_activity`: Historical frequency of earthquakes in each region
- Dropped redundant columns (`year`, `month`)
- Validated new features with correlation heatmap
- Notebook saved as: `Feature_Engineering/feature_creation_validation.ipynb`

---
### ✅ Trained the Model and Performed Model Evaluation

- Trained XGBoost regressor on cleaned dataset with engineered features
- Visualized feature importance using gain-based scores
- Identified top contributing features (e.g., cluster_id, depth, cluster_activity)
- Highlighted low-impact features to be excluded in future iterations
- Prepared for next steps: feature selection & hyperparameter tuning

### 🛠️ Up Next
- Visualize feature importances and prediction results
- Build a Streamlit frontend for user-friendly magnitude estimation

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
