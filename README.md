# Flight Fare Prediction System
Predict flight ticket prices using machine learning techniques based on various travel details.

## Introduction
  Airline companies use dynamic and complex pricing strategies, making it difficult for travelers to predict ticket prices. 
  This project aims to solve that problem using machine learning to estimate ticket prices in advance.

##  Objective
  The main objective of this project is to analyze how flight prices change and identify the key factors influencing those changes, then build a model to accurately predict the fare.

## Approach
  1. Imported necessary libraries and loaded the dataset.
  2. Performed Exploratory Data Analysis (EDA) to understand trends and relationships.
  3. Applied data preprocessing techniques:
     - OneHotEncoding
     - Label Encoding
     - Feature engineering (date/time breakdown)
  4. Identified important features using `ExtraTreeRegressor`.
  5. Trained multiple regression models:
     - Linear Regression
     - Random Forest Regression
  6. Compared models and selected the best-performing one.
  7. Applied hyperparameter tuning using `RandomizedSearchCV`.
  8. Saved the final model using `pickle` for future use.

##  Tech Stack
  - Python
  - Pandas, NumPy
  - Scikit-learn
  - Streamlit
  - Matplotlib, Seaborn
  - Pickle
## App Screenshot
<img width="910" height="720" alt="Image" src="https://github.com/user-attachments/assets/71a4fe61-5e1f-41f5-800c-fb589c122fa4" />

<img width="922" height="849" alt="Image" src="https://github.com/user-attachments/assets/65d05cac-1ee1-48ff-a8ba-5055d72fd97b" />

