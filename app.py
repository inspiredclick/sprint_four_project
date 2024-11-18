import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('vehicles_us.csv')
vehicles_us['date_posted'] = pd.to_datetime(vehicles_us['date_posted'], format='%Y-%m-%d')
vehicles_us['model_year'] = pd.to_numeric(vehicles_us['model_year'], errors='coerce').astype('Int64')
vehicles_us['cylinders'] = pd.to_numeric(vehicles_us['cylinders'], errors='coerce').astype('Int64')

st.title('Vehicle Listings Analysis')

new_listings_df = vehicles_us.sort_values('date_posted', ascending=False)
if st.checkbox('Show listings in excellent condition only'):
    new_listings_df = new_listings_df[new_listings_df['condition'] == 'excellent']

st.table(new_listings_df[['date_posted', 'model',  'model_year', 'price', 'condition', 'cylinders', 'fuel', 'odometer', 'transmission', 'type']].head(5))

st.header('Price Distribution by Model Year')

df = vehicles_us[['price', 'model_year']].dropna()
fig = px.scatter(df, x='model_year', y='price', labels={'model_year': 'Model Year', 'price': 'Price'})
st.plotly_chart(fig)

st.header('Number of Vehicles by Price')

fig = px.histogram(
    vehicles_us, 
    x='price',
    nbins=100, 
    range_x=(0, 100000),
  )
st.plotly_chart(fig)
