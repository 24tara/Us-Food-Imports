import streamlit as st

st.title("Analytics of US Food Imports")

import pandas as pd
#uploading and reading the cleaned dataset
dataset = pd.read_csv('FoodImports.csv')

