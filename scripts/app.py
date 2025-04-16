import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather=pd.read_csv("C:/Users/anisb/Desktop/Weather Data Analysis/data/weatherHistory_cleaned.csv")

#ui
st.title("Weather Dashboard 🌦️")
selected_var=st.selectbox("Choose a variable:",['Temperature (C)','Humidity','Summary'])

#plotting
fig,ax=plt.subplots(figsize=(10,6))
sns.lineplot(data=weather,x="Month",y=selected_var)
st.pyplot(fig)