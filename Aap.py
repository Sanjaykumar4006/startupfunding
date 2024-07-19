import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df= pd.read_csv('startup_cleaned.csv')
st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('Select One',['Startup Analysis','Overall Analysis','Investor'])
if option=='Overall Analysis':
    st.title('Overall Analysis')
elif option=='Startup Analysis':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('Find Investor Details',sorted(df['investors'].unique().tolist()))
    btn2=st.sidebar.button('Find Investor Details')
    st.title('Investor Analysis')
