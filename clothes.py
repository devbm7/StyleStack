import streamlit as st
from PIL import Image
from database import add_cloth_db, update_cloth_db, delete_cloth_db, get_clothes_by_category_db
import pandas as pd

def add_cloth():
    st.subheader("Add New Cloth")
    category = st.selectbox("Category", ["Pants", "Shirts", "Socks", "Others"])
    name = st.text_input("Name")
    image = st.file_uploader("Upload Image", type=["jpg", "png"])
    
    if st.button("Add Cloth"):
        if image and name:
            img = Image.open(image)
            add_cloth_db(category, img, name)
            st.success("Cloth added successfully!")
        else:
            st.error("Please provide all information.")

def update_cloth():
    st.subheader("Update Cloth Information")
    clothes = get_clothes_by_category_db()
    cloth_names = clothes['name'].tolist()
    cloth_to_update = st.selectbox("Select Cloth", cloth_names)
    
    if cloth_to_update:
        new_name = st.text_input("New Name", cloth_to_update)
        new_category = st.selectbox("New Category", ["Pants", "Shirts", "Socks", "Others"])
        new_image = st.file_uploader("Upload New Image", type=["jpg", "png"])
        
        if st.button("Update Cloth"):
            if new_image:
                img = Image.open(new_image)
            else:
                img = None
            update_cloth_db(cloth_to_update, new_name, new_category, img)
            st.success("Cloth updated successfully!")

def delete_cloth():
    st.subheader("Delete Cloth")
    clothes = get_clothes_by_category_db()
    cloth_names = clothes['name'].tolist()
    cloth_to_delete = st.selectbox("Select Cloth", cloth_names)
    
    if st.button("Delete Cloth"):
        delete_cloth_db(cloth_to_delete)
        st.success("Cloth deleted successfully!")

def get_clothes_by_category():
    st.subheader("View Clothes by Category")
    category = st.selectbox("Category", ["Pants", "Shirts", "Socks", "Others"])
    clothes = get_clothes_by_category_db(category)
    
    for _, row in clothes.iterrows():
        st.image(row['image'], caption=row['name'])
        st.write(f"Name: {row['name']}")
        st.write(f"Status: {row['status']}")
        st.write("---")
