# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import os
from joblib import dump

os.chdir('/Users/yashmange/Desktop/MASTER FILE/BIA PYTHON/CAPSTONE')
dataset = pd.read_csv('heart_disease.csv')

selected_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal']
X = dataset[selected_features]
Y = dataset['target']

model = RandomForestClassifier(n_estimators = 100, random_state=10)
model.fit(X,Y)

dump(model, 'Rf.joblib')
