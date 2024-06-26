# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:22:34 2024

@author: 91628
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu 


# loading the saved models

diabetes_model = pickle.load(open("Saved_models/Diabetes_model.sav",'rb'))
heart_model = pickle.load(open("Saved_models/Heartdisease_model.sav",'rb'))
parkinsons_model = pickle.load(open("Saved_models/Parkinson_model.sav",'rb'))


#Sidebar for navigating diseases 

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System using Machine Learning',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    
#Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    
    #Page title
    st.title('DIABETES PREDICTION using ML')
    
    
    #Getting input data from user
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
   
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
   
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    #Code for Prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            
    st.success(diab_diagnosis)    
        
        
        
        
# Heart Disease Prediction Page
   

if selected == 'Heart Disease Prediction':

    # page title
    st.title('HEART DISEASE PREDICTION using ML')

    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col1:
        cp = st.text_input('Chest Pain types')

    with col2:
        trestbps = st.text_input('Resting Blood Pressure')

    with col1:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col1:
        exang = st.text_input('Exercise Induced Angina')

    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col2:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The Person is having Heart disease'
        else:
            heart_diagnosis = 'The Person does not have any Heart disease'

    st.success(heart_diagnosis)



# Parkinson's Prediction Page

if selected == "Parkinson Prediction":

    # page title
    st.title('PARKINSON PREDICTION using ML')

    col1, col2, col3= st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col1:
        PPQ = st.text_input('MDVP:PPQ')

    with col2:
        DDP = st.text_input('Jitter:DDP')

    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')

    with col2:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The Person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The Person does Not have Parkinson's disease"

    st.success(parkinsons_diagnosis)    
