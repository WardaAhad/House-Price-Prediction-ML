# 🏠 House Price Prediction Using Regression

## 📌 Project Overview

This project predicts house prices using Machine Learning Regression techniques on the Ames Housing Dataset. It includes data preprocessing, exploratory data analysis (EDA), model training, and deployment using FastAPI and Streamlit.

---

## 🚀 Features

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Simple Linear Regression
* Multiple Linear Regression
* Polynomial Regression
* Model Performance Comparison
* FastAPI Backend
* Streamlit Frontend
* Real-time House Price Prediction

---

## 📂 Project Structure

```
House-Price-Prediction-Using-Regression
│
├── backend/
│   ├── app.py
│   └── final_model.pkl
│
├── frontend/
│   └── app.py
│
├── notebook/
│   └── House_Price_Prediction.ipynb
│
├── train.csv
├── requirements.txt
├── README.md

```

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* FastAPI
* Streamlit
* Joblib

---

## 📊 Dataset

* Ames Housing Dataset
* File: `train.csv`

---

## 📈 Machine Learning Models

* Simple Linear Regression
* Multiple Linear Regression
* Polynomial Regression

---

## 🎯 Input Features

* OverallQual
* GrLivArea
* GarageCars
* GarageArea
* TotalBsmtSF
* 1stFlrSF
* FullBath
* TotRmsAbvGrd
* YearBuilt
* YearRemodAdd

---

## ▶️ Run Backend

```bash
cd backend
uvicorn app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

```bash
cd frontend
streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

## 📌 Future Improvements

* Hyperparameter Tuning
* Model Optimization
* Cloud Deployment
* User Authentication
* Better UI Design

---

## 👩‍💻 Author

**Warda Ahad**

BS Artificial Intelligence Student


