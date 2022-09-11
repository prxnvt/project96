import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(page_title = "Census Visualization Web App",
                   page_icon = "random", layout = "centered", initial_sidebar_state = "auto")

@st.cache()
def load_data():
    df = pd.read_csv("adult.csv", header=None)
    df.head()
    column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation',
                  'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    for i in range(df.shape[1]):
        df.rename(columns={i:column_name[i]},inplace=True)
    df.head()
    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)
    df.dropna(inplace=True)
    df.drop(columns='fnlwgt',axis=1,inplace=True)
    return df
census_df = load_data()

st.title("Census Visualization Web App")
st.write("Interactive visualizer for a census dataframe")
st.header("View Data")
with st.expander("View Dataset"):
    st.dataframe(census_df)
col1, col2, col3 = st.columns(3)
with col1:
    if st.checkbox("Show all Column Names"):
        st.table(census_df.columns)
with col2:
    if st.checkbox("View column data-type"):
        st.table(census_df.dtypes)
with col3:
    if st.checkbox("View column data"):
        user_column_selected = st.selectbox("Select Columns", tuple(census_df.columns))
        st.write(census_df[user_column_selected])
if st.checkbox("Show Summary"):
    st.table(census_df.describe())
#

