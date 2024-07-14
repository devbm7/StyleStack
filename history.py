import streamlit as st
from database import get_clothes_by_category_db, get_laundry_history

def display_history():
    st.subheader("Clothes History")
    
    clothes = get_clothes_by_category_db()
    cloth_names = clothes['name'].tolist()
    cloth_to_view = st.selectbox("Select Cloth", cloth_names)
    
    if cloth_to_view:
        history = get_laundry_history(cloth_to_view)
        st.write(history)
