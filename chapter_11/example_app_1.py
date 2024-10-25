import streamlit as st
 
# Title of the app
st.title("Hello World App")
 
# Display a text message
st.write("Welcome to your first Streamlit app!")
 
# Create a button widget
if st.button("Click me!"):
    st.write("Button clicked!")
