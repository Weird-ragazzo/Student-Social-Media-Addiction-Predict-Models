# 📘 Student Social Media Addiction Predictors (Individual Models)

This repository contains **4 individual Streamlit applications**, each built using a different machine learning model to predict student social media addiction based on various personal, academic, and lifestyle features.

---

## 🚀 Models Included

Each model is saved in its own `.pkl` file and connected to a dedicated `Streamlit` app for demonstration and testing.

| Model                | File Name                            | Accuracy |
|---------------------|--------------------------------------|----------|
| Logistic Regression | `student_addiction_model_LogReg.pkl` | 99.0%    |
| Random Forest       | `model_RandomForest.pkl`             | 100%     |
| XGBoost             | `model_XGBoost.pkl`                  | 99.2%    |
| LightGBM            | `model_LightGBM.pkl`                 | 99.4%    |

---

## 📊 Features

- Modern, interactive UI using Streamlit  
- Individual prediction apps for each model  
- User input form for 12+ features  
- Result display with visual feedback  
- Model accuracy info embedded in each app

---

## 🧠 Dataset & Features

The model was trained on a dataset with the following features:

- Gender  
- Academic Level  
- Average Daily Usage (hours)  
- Affects Academic Performance  
- Sleep Hours per Night  
- Mental Health Score (1–10)  
- Relationship Status  
- Conflicts Over Social Media  
- Most Used Social Media Platform (12 options)

**Target variable:** `Addicted Score (binary)`

---

## 👨‍💻 Author

**Dhruv Raghav**
