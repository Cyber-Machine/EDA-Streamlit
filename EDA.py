import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Page Confurigation
st.set_page_config(
    page_title = 'Home'
)
# Title
st.markdown('''
## **Exploratory Data Analysis with Python**
### So what is EDA ?
- Exploratory Data Analysis is a part in Data Analysis of performing initial investigations in data in order to discover patterns , check for outliers or to make hypothesis and check assumptions with the **power** of Statistics and graphical representations.
''')

# SideBar 
with st.sidebar.header('Upload CSV Data'):
    uploaded_file = st.sidebar.file_uploader("Drag and drop your CSV Files Here")

# Context 
st.markdown('''
### Let's begin with an Example Data :
To to EDA with your data, upload files in SideBar.
''')


# Pandas_profiling
if uploaded_file is not None:
    # Reading CSV
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df , explorative = True)
    st.table(df.head())
    st_profile_report(pr)
else :
    st.info('Awaiting File to be Uploaded')
    if st.button('Example DataSet'):
        @st.cache
        def load_data():
            csv = pd.read_csv('Sample - Superstore.csv')
            return csv
        df = load_data()
        pr = ProfileReport(df , explorative = True)
        st.header("Example of SuperStore Orders -->")
        st.table(df.head())
        st_profile_report(pr)

