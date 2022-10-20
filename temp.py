
"""Spyder Editor
This is a temporary script file.
"""
import numpy as np
import pickle
#import streamlit
#loading the saved model
loaded_model=pickle.load(open('E:/New folder/trained_model.sav','rb'))
input_data=(4,110,92,0,0,37.6,0.191,30)
input_data_as_numpy=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
if(prediction[0]==0):
  print('the person is non-diabitic')
else:
  print('the person is diabitic')
  
  