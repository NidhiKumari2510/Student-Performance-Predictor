# Student Performance Predictor

## Overview

This project uses Machine Learning to predict a student's final academic grade (G3) based on demographic, academic, and social factors.

The model is trained on the Student Performance Dataset and uses Random Forest Regression to learn relationships between study habits, previous grades, family background, and final performance.

## Features

* Data preprocessing using Pandas
* Categorical feature encoding using One-Hot Encoding
* Train-Test Split for model evaluation
* Random Forest Regressor implementation
* Model persistence using Pickle
* Performance evaluation using R² Score

## Dataset Features

Examples of input features:

* Study Time
* Absences
* Family Support
* Internet Access
* Previous Grades (G1, G2)
* Parental Education
* Health Status

Target Variable:

* G3 (Final Grade)

## Results

Model Achieved:

* R² Score: 0.805

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Pickle

## Project Structure

Student-Performance-Predictor/

├── data/

├── models/

├── train.py

├── predict.py

├── requirements.txt

└── README.md

## Future Improvements

* Hyperparameter Tuning
* Feature Importance Analysis
* Interactive Prediction Interface
* Model Comparison with Other Algorithms
