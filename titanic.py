import streamlit as st
from joblib import load 

st.title("Titanic survival prediction")

pClass = st.number_input("Enter Pclass (1,2,3)")
gender = st.radio("Female/Male" , [0,1])
age = st.number_input("Enter age")
sibsp = st.number_input("Sibsp (0,1,2,3)")
parch = st.number_input("Enter Parch (0,1,2)")
fare = st.number_input("Enter fare")

clicked = st.button("Get Prediction")

# This is a sklearn model
model = load('Titanic_model.joblib')

if(clicked == True):
    # Take the data and predict the survival/dead
    data = [pClass , gender , age , sibsp , parch , fare]
    print(data)

    pred = model.predict([data])
    print(pred[0])
    if(pred[0] == 0):
        st.header("Not Survived")
    else:
        st.header("Survived")
