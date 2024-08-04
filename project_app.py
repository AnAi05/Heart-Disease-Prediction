#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:42:27 2024

@author: yashmange
"""

import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder
import os

os.chdir('/Users/yashmange/Desktop/MASTER FILE/BIA PYTHON/CAPSTONE')
model = load('Rf.Joblib')

st.title("Heart Disease Prediction")


#input fields : 
    
    
st.header("Enter Health info")

age = st.number_input("Age",min_value=0,max_value=100,value=1)
sex = st.selectbox("Gender",('Female', 'Male'))
cp = st.selectbox("CHEST PAIN - Chest Pain type : 0: Typical angina (caused by physical exertion or stress) - 1: Atypical angina (not typical; may still indicate heart problems); 2: Non-anginal pain (may not be related to heart conditions); 3: Asymptomatic (no chest pain)",('0 Typical Angina', '1 Atypical Angina', '2 Non-Anginal Pain', '3 Asymptomatic'))
trestbps = st.number_input("TRESTBPS - Resting Blood Pressure (trestbps)",min_value=0,max_value=300,value=1)
chol = st.number_input("CHOL - Serum Cholestoral (chol) mg/dl", min_value=0, max_value=800, value=1)
fbs = st.selectbox(" FBS - Is your Fasting Blood Sugar (fbs) > 120 mg/dl ? ",('No - Below 120', 'Yes - Above 120'))
thalach = st.number_input("THALACH - Maximum Heart Rate Achieved (thalach)", min_value=0, max_value=400, value=1)
restecg = st.selectbox("RESTECG - Resting electrocardiographic results (values 0, 1, 2) - 0: Normal; 1: Abnormal (showing probable or definite left ventricular hypertrophy); 2: Abnormal (showing ST-T wave abnormality)",('0: Normal', '1: Abnormal (showing probable or definite left ventricular hypertrophy)', '2: Abnormal (showing ST-T wave abnormality)'))
exang = st.selectbox("EXANG - xercise-induced angina (binary) : Indicates whether angina (chest pain) was induced by physical exercise - Yes or No",('Yes','No'))
oldpeak = st.number_input("OLDPEAK - ST depression induced by exercise relative to rest (Oldpeak) ", format="%.2f", value = 1.0, max_value=999999999999.00, min_value=0.00, key = 'number_slider')
slope = st.number_input("SLOPE - Slope of the ST Segment (slope)", min_value=0, max_value=4, value=1)
ca = st.selectbox("CA - Number of major vessels (0-4) colored by flourosopy: This refers to the number of major blood vessels (0 to 4) visible under fluoroscopy that have been colored by a contrast agent", ('0','1','2','3','4'))
thal = st.selectbox("THAL - Thalassemia is a genetic disorder that affects hemoglobin production. Select from - Normal ; Fixed defect (no blood flow in some part of the heart) ; Reversible defect (blood flow is observed but not normal)",('0 Normal','1 Fixed Defect','2 Reversable Defect'))

label_mapping = {'Female':0,'Male':1,'0 Typical Angina':0,'1 Atypical Angina':1,'2 Non-Anginal Pain':2,'3 Asymptomatic':3,'No - Below 120':0,'Yes - Above 120':1,'0: Normal':0, '1: Abnormal (showing probable or definite left ventricular hypertrophy)':1, '2: Abnormal (showing ST-T wave abnormality)':2,'Yes':1,'No':0,'0':0,'1':1,'2':2,'3':3,'4':4,'0 Normal':0,'1 Fixed Defect':1,'2 Reversable Defect':2}

sex = label_mapping[sex]
cp = label_mapping[cp]
fbs = label_mapping[fbs]
thal = label_mapping[thal]
restecg = label_mapping[restecg]

exang = label_mapping[exang]
ca = label_mapping[ca]

prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

st.header("prediction result")
if prediction[0] == 0:
    st.success("Heart Disease Most likely Not possible")
else:
    st.error("Heart Disease Most likely possible")
