import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
 
# Title
st.title("Matplotlib Chart in Streamlit")
 
# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)
 
# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)
 
# Display the plot in the Streamlit app
st.pyplot(fig)
