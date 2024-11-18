import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

columns = ['Quarter','Garda Division','Type of Offence']
df = pd.read_csv('data/cso_data.csv',usecols=columns)

df['Q'] = df['Quarter'].str[-2:]
df['Year'] = df['Quarter'].str[0:4]
df.rename(columns={'Quarter':'Year_Quarter'},inplace=True)
df['Garda Division'] = df['Garda Division'].str.replace('Garda Division','',regex=False)
df['Garda Division'].str.strip()

df = df[['Year_Quarter','Year','Q','Garda Division','Type of Offence']]
st.dataframe(df,use_container_width=True,hide_index=True)