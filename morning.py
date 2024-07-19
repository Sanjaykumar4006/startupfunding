import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import  streamlit as st
df=pd.read_csv('startup_cleaned.csv')
#df.info()
# changing required data type
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['year']=df['date'].dt.year
total=round(df['amount'].sum())
max=df['amount'].max()
min=df['amount'].min()
mean=round(df['amount'].mean())

# writing code for important metrics and yoy
def load_overall_analysis():
    st.header('Overall Analysis')
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total Investment", str(total) + "Cr")
    with col2:
        st.metric("Maximum Investment", str(max) + "Cr")
    with col3:
        st.metric("Minimum",str(min)+"Cr")
    with col4:
        st.metric("Average", str(mean) + "Cr")
    st.header("MoM Graph")
    g_options=st.selectbox("Select One",["Revenu","Count"])
    if g_options=="Revenu":
        x = df.groupby(['year'])[['amount']].sum()
        fig, ax = plt.subplots()
        ax.plot(x.index, x.values)
        st.pyplot(fig)






# company wise analysis
def load_startup_analysis():
    st.header('Startup Analysis')

# investor wise Analysis

def load_investor_analysis(investor):
    st.title(investor)
    top_5=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city',
                                                                              'amount']]
    st.dataframe(top_5)





options=st.sidebar.selectbox("Select One",["Investor","Startup","Overall"])
if options=="Overall":
    load_overall_analysis()
elif options=="Startup":
     load_startup_analysis()
else:
    selected_investor = st.sidebar.selectbox('Select StartUp',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
if btn2:
    load_investor_analysis(selected_investor)