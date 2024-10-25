# Project: Real-Time Data Dashboard with Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("sample_data.csv")
 
# Display the first few rows of the dataset
st.write(data.head())

# Add a slider to filter by age
age_filter = st.slider("Select age range", 18, 50, (20, 40))
 
# Filter the data by age
filtered_data = data[(data["Age"] >= age_filter[0]) & (data["Age"] <= age_filter[1])]
 
# Add a dropdown to filter by city
city_filter = st.selectbox("Select city", data["City"].unique())
 
# Filter the data by city
filtered_data = filtered_data[filtered_data["City"] == city_filter]
 
# Display the filtered data
st.write(filtered_data)
 
# Plot the age distribution of the filtered data
fig, ax = plt.subplots()
ax.hist(filtered_data["Age"], bins=10, edgecolor="black")
 
# Add labels and title
ax.set_title("Age Distribution")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")
 
# Display the plot in Streamlit
st.pyplot(fig)
