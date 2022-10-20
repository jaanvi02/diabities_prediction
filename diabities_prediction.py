# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 00:19:40 2022

@author: hp
"""
import numpy as np
import pickle

import streamlit as st
#loading the saved model

loaded_model=pickle.load(open('D:/cpp/trained_model.sav','rb'))
#input_data=(4,110,92,0,0,37.6,0.191,30)
def diabitiesprediction(input_data): 
     input_data_as_numpy=np.asarray(input_data)
     
     input_data_reshaped=input_data_as_numpy.reshape(1,-1)
     prediction=loaded_model.predict(input_data_reshaped)
     if(prediction[0]==0):
         return 'the person is non-diabitic'
     else:
         return 'the person is diabitic'

def main():
    st.title('diabities prediction web app')
    pregnancies=st.text_input('number of pregnancies')
    glucose=st.text_input('glucose level')
    blood_pressure=st.text_input('blood pressure level')
    skinthickness=st.text_input('skin thickness value')
    insulin=st.text_input('insulin value')
    BMI=st.text_input('BMI value')
    diabitiesPedigreeFunction=st.text_input('Diabities Pedigree Function value')
    age=st.text_input('enter age')
    diagnosis=''
    if st.button('diabities test result'):
        diagnosis=diabitiesprediction([pregnancies,glucose,blood_pressure,skinthickness,insulin,BMI,diabitiesPedigreeFunction,age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()

    