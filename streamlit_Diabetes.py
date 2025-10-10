import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\TOSHIBA\python\60hrcourse\projects\Diabetes Prediction\trained_model.sav','rb'))


# creating a func for prediction
def diabetes_prediction(input_data):
    
    input_data = (4,110,92,0,0,37.6,0.191,30)

    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction) 

    if (prediction[0] == 0):
        return "The person is not diabetic"
    else:
        return "The person is diabetic"


def main():
    st.title('Diabetes Prediction Web App')

    #getting the input data from user 

    Pregnancies = st.text_input('Number of Pregnancies ')
    Glucose = st.text_input('Whats the Glucose  = ')
    BloodPressure = st.text_input('whats the BloodPressure ')
    SkinThickness = st.text_input('whats the SkinThickness ')
    Insulin = st.text_input('whats the Insulin ')
    BMI = st.text_input('whats the BMI ')
    DiabetesPedigreeFunction = st.text_input('whats the DiabetesPedigreeFunction ')
    Age = st.text_input('whats the Age ')


    # code for prediction.
    diagnosis = ''

    # creating a button for prediction
    if st.button(" Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()

    