# 🏠 Real Estate Price Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-Final%20Model-green?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=flat&logo=streamlit)
![R2 Score](https://img.shields.io/badge/R²%20Score-90%25-brightgreen?style=flat)
![MAE](https://img.shields.io/badge/MAE-Rs.%200.50%20Cr-brightgreen?style=flat)

An ML-powered web application that predicts residential property prices using advanced machine learning techniques. Built to help users make data-driven investment and pricing decisions.

---

## 📌 Project Overview

This project predicts residential property prices based on key real estate factors such as location, area, furnishing status, amenities, and engineered features. The final model achieves an **R² score of 90%** and **MAE of Rs. 0.50 Cr** after hyperparameter tuning with XGBoost.

---

## 🚀 Live Demo

🔗 [Try the App on Streamlit Cloud](https://your-streamlit-link.streamlit.app)

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| ML Library | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web App | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📂 Project Structure

```
real-estate-price-predictor/
│
├── app.py                  # Streamlit web application
├── model.pkl               # Trained XGBoost model
├── pipeline.pkl            # Scikit-learn pipeline
├── notebooks/
│   ├── EDA.ipynb           # Exploratory Data Analysis
│   ├── preprocessing.ipynb # Data Cleaning & Feature Engineering
│   └── model_training.ipynb# Model Training & Evaluation
├── data/
│   └── dataset.csv         # Raw dataset (~3000 properties)
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

- **Size:** ~3,000 residential property records
- **Source:** Gurgaon real estate listings
- **Key Features:** Location, Area, Bedrooms, Furnishing, Floor, Age, Amenities

---

## ⚙️ Feature Engineering

Two key features were engineered to improve model performance:

| Feature | Description |
|---|---|
| **Luxury Score** | Composite score based on premium amenities like pool, gym, parking |
| **Additional Rooms** | Count of extra rooms like study, servant, store rooms |

These engineered features contributed significantly to the **32% accuracy improvement** over baseline.

---

## 🤖 Model Comparison

All models were trained and evaluated on the same train-test split. Results before and after optimization:

| Model | R² Score | MAE (Cr) |
|---|---|---|
| **XGBoost** ✅ | **0.9035** | **0.5265** |
| Random Forest | 0.8994 | 0.5002 |
| Gradient Boosting | 0.8814 | 0.5788 |
| Decision Tree | 0.8010 | 0.7120 |
| AdaBoost | 0.7862 | 0.8483 |
| Linear Regression | 0.7345 | 1.1876 |
| Ridge Regression | 0.7345 | 1.1909 |
| SVR | 0.6645 | 1.4066 |
| LASSO | 0.0141 | 1.5495 |

> **XGBoost selected as final model** based on highest R² score and lowest MAE after hyperparameter tuning.

---

## 📈 Model Performance

| Metric | Baseline | Final Model | Improvement |
|---|---|---|---|
| R² Score | 58% | **90%** | +32% |
| MAE | Rs. 2.85 Cr | **Rs. 0.50 Cr** | -82% |

---

## 🔑 Key Steps

1. **Data Cleaning** — Handled missing values, outliers, and inconsistent entries
2. **Feature Engineering** — Created Luxury Score and Additional Rooms features
3. **Feature Selection** — Selected top impactful variables using correlation and importance scores
4. **Pipeline Design** — Built Scikit-learn pipeline for preprocessing + model
5. **Hyperparameter Tuning** — Optimized XGBoost parameters using GridSearchCV
6. **Deployment** — Deployed on Streamlit Cloud for real-time predictions

---

## 💡 Key Insights

- **XGBoost outperformed** all 8 other models with R² of 90%
- **LASSO performed worst** (R² = 0.014) — indicating non-linear relationships in data
- **Luxury Score** was among top 3 most important features
- **Location and Area** remained strongest predictors of property price
- **82% reduction in MAE** achieved through tuning and feature engineering

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/prasadkate1307/real-estate-price-predictor.git

# Navigate to project folder
cd real-estate-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---


## 👤 Author

**Prasad Kate**
- GitHub: [@prasadkate1307](https://github.com/prasadkate1307)
- LinkedIn: [prasad-kate](https://www.linkedin.com/in/prasad-kate)
- Email: prasadkate1307@gmail.com
