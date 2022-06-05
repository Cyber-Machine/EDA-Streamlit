import streamlit as st
import pandas as pd
# import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(
    page_title = 'Plots for the Example Dataset'
)

def load_data():
        csv = pd.read_csv('Sample - Superstore.csv')
        return csv
df = load_data()
st.header("Make Interactive plots with Superstore Data :")
st.subheader("Select the type of Plot You want to Make :")
plot_type = st.selectbox("Choose your type of plot" ,("Bar", "Line Chart" , "Area Chart"))
if plot_type == "Line Chart":
    
    x_options = ['Sales','Quantity','Discount','Profit']
    x_axis = st.selectbox('Select X Axis ', x_options)
    y_options = ['Sales','Quantity','Discount','Profit']
    y_axis = st.multiselect('Select Y Axis ', y_options)
    if st.button('Plot'):
        data = df.groupby(x_axis)[y_axis].agg(sum)
        st.line_chart(data)
elif plot_type =="Area Chart":
    x_options = ['Sales','Quantity','Discount','Profit']
    x_axis = st.selectbox('Select X Axis ', x_options)
    y_options = ['Sales','Quantity','Discount','Profit']
    if(x_axis in y_options):
        y_options.remove(x_axis)
    y_axis = st.multiselect('Select Y Axis ', y_options)
    if st.button('Plot'):
        data = df.groupby(x_axis)[y_axis].agg(sum)
        st.area_chart(data)