#importing relevant libraries
#streamlit to use cide space and build on codespace 
import streamlit as st
#for python language
import pandas as pd

#title
st.title("DASHBOARD: Analytics of US Food Imports")
#warning message displayed
st.warning("WARNING: Data in this Dashbaord may be sensitive/ classified. ")

#naming my file as data
#read the csv file
#latin1 allows for special characters 
data = pd.read_csv("FoodImports.csv", encoding='latin1')

#header for basic info
st.header("Basic inforamtion on the dataset")


#using header function  to display the first 10 rows of my dataset
st.subheader("First 10 Rows of the Dataset")
#create a table for top 10
st.dataframe(data.head(10))

st.subheader("Rows of the Dataset")
# sldier for ampount of rows in dataset
num_rows = st.slider("drag to display number of rows to view:", min_value=1, max_value=15, value=5)
# Display rows
st.dataframe(data.head(num_rows))
#st.success("success") 


st.subheader("Check to See Column Names")
#function to see names
if st.button("View Columns"):
    st.write(list(data.columns))


st.subheader("Basic Satistics")
st.write(data.describe())


#this function displays the amount of missing data instances in each variable
#alls will count how many on the side because of the word sum
data.isnull().sum()
st.subheader("Missing Data In Each Instance")
st.write(data.isnull().sum())


st.subheader("Data Points")
#how many data points there are
st.write(data.shape)


st.subheader("Basic Statistics on  Catagorical Features")
#this function creates stats on the catagorical varaibles bin the dataset
st.write(data.describe(include='object'))


# this breaks down the options in the varaible and tell"Country"s you the data type
#st.subheader("Unique Features of Commodity")
#st.write(data['Commodity'].unique())

#st.subheader("Unique Features of Country")
#st.write(data['Country'].unique())

#st.subheader("Unique Features of Unit of Measure")
#st.write(data['Unit of Measure'].unique())

#st.subheader("Unique Features of Category")
#st.write(data['Category'].unique())

#st.subheader("Unique Features of Subcategory")
#st.write(data['Subcategory'].unique())

#st.subheader("Unique Features of Row Number")
#st.write(data['Row Number'].unique())

#st.subheader("Unique Features of Year Number")
#st.write(data['Year Number'].unique())

#st.subheader("Unique Features of Value")
#st.write(data['Value'].unique())


st.subheader("Select Columns to View Unique Values")
#variable for multiselect option
options = ['Commodity', 'Country', 'Unit of Measure', 'Category', 'Subcategory', 'Row Number', 'Year Number', 'Value']
#new variable once cols have been chosen
selected_columns = st.multiselect("Select columns:", options)
#for loop for only chosen cols
for col in selected_columns:
    st.subheader(f"Unique Features: {col}")
    st.write(data[col].unique())


#creating visualisations for the dashboards
st.title("Findings")
#st.subheader("Top Countries Importing Food into US")


#created a variable 
#data by countires and have looked at imports column
top_countries = data.groupby('Country')['Value'].sum().sort_values(ascending=False).head(10)
st.subheader("Top 10 Countries with highest Food Imports")
#creates a bar chart
st.bar_chart(top_countries)
st.caption ("The top 3 countries that import into the US are: Canada, Chile and China")


#data by countires and have looked at imports column
lowest_countries = data.groupby('Country')['Value'].sum().sort_values(ascending=True).head(10)
st.subheader("Top 10 Countries with Lowest Food Imports")
st.bar_chart(lowest_countries)
st.caption( "The lowest 3 countires that import into the US are: Benin, Bulgaria and Croatia")


st.subheader("Line Chart of Total Imports Over the Years")
#checkbox function to show trend
#if statement 
if st.checkbox("Check to see trends"):
#message that shows while loading
   #st.spinner("waiting...")
#data by year, also then sumed value
    trend_data = data.groupby('Year Number')['Value'].sum().reset_index()
# displays chart
    st.line_chart(trend_data.set_index('Year Number'))


st.success("You have reached the end ") 
st.title(":)")
#st.balloons()














