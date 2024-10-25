import streamlit as st
 
# Title of the app
st.title("Simple Interactive App")
 
# Create a slider widget for user input
age = st.slider("Select your age", 18, 100)
 
# Create a text input widget
name = st.text_input("Enter your name")
 
# Display the result
st.write(f"Hello {name}, you are {age} years old!")
