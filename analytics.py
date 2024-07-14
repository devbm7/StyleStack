import streamlit as st
from database import get_clothes_by_category_db, get_laundry_history
import pandas as pd

def display_analytics():
    st.subheader("Analytics")
    
    clothes = get_clothes_by_category_db()
    st.write("### Clothes Summary")
    st.write(clothes.groupby('category').size().reset_index(name='counts'))
    
    st.write("### Laundry Actions")
    all_history = pd.DataFrame()
    for _, row in clothes.iterrows():
        history = get_laundry_history(row['name'])
        all_history = pd.concat([all_history, history])
    
    st.write(all_history.groupby('action').size().reset_index(name='counts'))
