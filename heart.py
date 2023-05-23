import pickle
import streamlit as st

# Membaca dataset
heart_model = pickle.load(open('heart.sav', 'rb'))


# Prediksi Gagal Jantung
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Sex = st.text_input('Sex (Initial)')
    
    with col3:
        ChestPainType = st.text_input('Chest Pain Type')
    
    with col1:
        RestingBP = st.text_input('Resting BP')
    
    with col2:
        Cholesterol = st.text_input('Cholesterol')
    
    with col3:
        FastingBS = st.text_input('Fasting BS')
    
    with col1:
        RestingECG = st.text_input('Resting ECG')
    
    with col2:
        MaxHR = st.text_input('Max HR')
    
    with col3:
        ExerciseAngina = st.text_input('Exercise Angina')
    
    with col1:
        Oldpeak = st.text_input('Oldpeak')
    
    with col2:
        ST_Slope = st.text_input('ST Slope')
    
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Hasil Tes Gagal Jantung'):
        heart_prediction = diabetes_model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is diabetic'
        else:
          heart_diagnosis = 'The person is not diabetic'
        
    st.success(heart_diagnosis)