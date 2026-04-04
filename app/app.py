import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

st.set_page_config(page_title="House Price Predictor",layout="wide",
    page_icon="🏠")

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, "Real_estate_df.pkl"), "rb") as file:
    df = pickle.load(file)

with open(os.path.join(BASE_DIR, "Real_estate_pipeline.pkl"), "rb") as file:
    pipeline = pickle.load(file)
        
st.image("real-estate.jpg", use_container_width=True)   
st.title("🏠 Real Estate Price Predictor")
  

st.markdown("### Predict property prices instantly using ML")
st.divider()

st.sidebar.header("📝 Enter Property Details")

city = st.selectbox('Select City', ['Gurgaon'])

col1,col2=st.columns(2)
with col1: 
    property_type=st.selectbox('Property_type',df['F/H'].unique().tolist()) 
    
with col2:
    sector=st.selectbox('Sector',df['sector'].unique().tolist()) 
    
col1,col2,col3=st.columns(3) 

with col1:
    bathrooms= float(st.selectbox('No. of Bathrooms',sorted(df['bathroom'].unique().tolist()))) 
with col2: 
    bedrooms= float(st.selectbox('No. of Bedrooms',sorted(df['bedRoom'].unique().tolist())))

with col3:
    balcony= st.selectbox('No. of Balconies',sorted(df['balcony'].unique().tolist())) 
    
col1,col2=st.columns(2) 

with col1: 
    age_Possession= st.selectbox('Age Possession',df['agePossession'].unique().tolist()) 

with col2:
    furnishing_type =st.selectbox('Furnishing Type',df['furnishing_type'].unique().tolist())
    
total_area_sqft=int(st.number_input('Select Area in sqft',value=1000,step=50)) 

col1,col2=st.columns(2) 

with col1:
    additional_rooms=st.selectbox('No. of Additional Rooms',sorted(df['additional_room_count'].unique().tolist())) 

with col2: 
    luxury_category= st.selectbox('Luxury Category',df['luxury_cat'].unique().tolist()) 

    sorted(df['additional_room_count'].unique().tolist())



st.divider()
    
col1, col2, col3 = st.columns(3)

with col2:
    st.markdown("""
    <style>
    div.stButton > button {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        color: white;
        border: none;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)


if st.button('Predict'):
    # make dataframe
    data = [[property_type, sector,total_area_sqft, bedrooms, bathrooms, balcony, age_Possession, furnishing_type,additional_rooms,luxury_category]]
    columns = ['F/H', 'sector', 'total_area_sqft', 'bedRoom', 'bathroom',
       'balcony', 'agePossession', 'furnishing_type', 'additional_room_count',
       'luxury_cat']
    
    one_df=pd.DataFrame(data,columns=columns)
    st.dataframe(one_df)
    # predict
    base_price=np.expm1(pipeline.predict(one_df))[0]
    
    low=base_price- 0.26
    high=base_price+ 0.26
    
    st.success(f"Price of Property is between {low:0.2f} Cr and {high:0.2f} Cr")
    
    