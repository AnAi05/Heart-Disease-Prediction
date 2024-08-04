# Heart Disease Prediction

## Project Overview

This project aims to build and evaluate machine learning models to predict the presence of heart disease based on various medical features. The primary goal is to achieve high accuracy while prioritizing sensitivity (recall) to minimize the risk of misdiagnosing individuals with heart disease. This predictive model can assist healthcare professionals in identifying individuals at risk of heart disease.

## Dataset

The project utilizes the Heart Disease Dataset from the UCI Machine Learning Repository. The dataset contains 14 features and a binary target variable indicating the presence or absence of heart disease. The features include:
- Age
- Sex
- Chest pain type (4 values)
- Resting blood pressure
- Serum cholesterol levels
- Fasting blood sugar (binary)
- Resting electrocardiographic results (3 values)
- Maximum heart rate achieved
- Exercise-induced angina (binary)
- ST depression induced by exercise relative to rest
- Slope of the peak exercise ST segment (3 values)
- Number of major vessels colored by fluoroscopy (0-4)
- Thalassemia (3 values)
- Target variable (0 for absence and 1 for presence of heart disease)

## Project Stages

1. **Data Exploration and Preprocessing**
   - Load the dataset and familiarize yourself with the features.
   - Check for missing values and handle them appropriately.
   - Perform exploratory data analysis (EDA) to understand feature distributions and relationships.
   - Normalize or standardize the data as needed.

2. **Model Building**
   - Split the data into training and testing sets.
   - Train multiple machine learning models, including Logistic Regression, Support Vector Machine, Naive Bayes, Decision Tree, Random Forest, XGBoost, and Neural Network.
   - Use Grid Search for hyperparameter tuning to optimize model performance.

3. **Model Evaluation**
   - Evaluate model performance using accuracy, precision, recall, F1-score, and confusion matrix.
   - Compare the performance of different models.

4. **Model Selection**
   - Select the best-performing model based on evaluation metrics.
   - Fine-tune the selected model for improved performance.

5. **Documentation**
   - Document the methodology, data sources, and technical specifications of the predictive model for future reference and scalability.

## Results

The accuracy scores achieved by various models are:
- Logistic Regression: **xx.xx%**
- Support Vector Machine: **xx.xx%**
- Naive Bayes: **xx.xx%**
- Decision Tree: **xx.xx%**
- Random Forest: **xx.xx%**
- XGBoost: **xx.xx%**
- Neural Network: **xx.xx%**

The best performing model was [Model Name] with an accuracy of **xx.xx%**.

## Conclusion

The developed predictive model demonstrates high accuracy and sensitivity in predicting the presence of heart disease. This tool can be valuable for healthcare professionals in early detection and risk assessment, potentially improving patient outcomes.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
