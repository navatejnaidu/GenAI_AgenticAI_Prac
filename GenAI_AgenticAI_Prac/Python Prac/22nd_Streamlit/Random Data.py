import streamlit as st
import pandas as pd 
import numpy as np 

st.title("Random Data")
st.write("This is a simple app to demonstrate the basic functionalities of Streamlit.")
st.sidebar.header("User Input Features")

user_name = st.sidebar.text_input("What is your name?", "P.Navatej Naidu")

age = st.sidebar.slider("Select your age", 1, 100)

favorite_color = st.sidebar.selectbox("What is your favorite color?", ["Blue", "Red", "Green", "Yellow"])

st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favorite color is {favorite_color}.")
st.subheader("random data:")

data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

if st.button("Bye"):
    st.write("Goodbye!")