import streamlit as st
import pickle
import numpy as np

def load_model():
  with open('deployment.pkl','rb') as file:
    data = pickle.load(file)
  return data

data = load_model()

model = data['model']
le_Sex = data['le_Sex']
le_Embarked = data['le_Embarked']

st.title("Titanic Survival")

Sex = ('male', 'female')
Embarked = ('S', 'C', 'Q')
Pclass = (1, 2, 3)

Pclass = st.selectbox('Pclass', Pclass)
Sex = st.selectbox('Sex', Sex)
Age = st.number_input('Age')
Embarked = st.selectbox('Embarked', Embarked)

ok = st.button("Survival Probability")
if ok:
   X = np.array([[Pclass,Sex,Age,Embarked]])
   X[:,1] = le_Sex.transform(X[:,1])
   X[:,3] = le_Embarked.transform(X[:,3])
   Survival = model.predict(X)
   if Survival == 1:
     st.write(" You will Survive.")
   else:
     st.write("You will not Survive.")
