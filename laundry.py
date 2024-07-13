import streamlit as st
from database import update_cloth_status, get_clothes_by_status

def send_to_laundry():
    st.subheader("Send Cloth to Laundry")
    clothes = get_clothes_by_status('In Closet')
    cloth_names = clothes['name'].tolist()
    cloth_to_laundry = st.selectbox("Select Cloth", cloth_names)
    
    if st.button("Send to Laundry"):
        update_cloth_status(cloth_to_laundry, 'In Laundry')
        st.success("Cloth sent to laundry!")

def return_from_laundry():
    st.subheader("Return Cloth from Laundry")
    clothes = get_clothes_by_status('In Laundry')
    cloth_names = clothes['name'].tolist()
    cloth_from_laundry = st.selectbox("Select Cloth", cloth_names)
    
    if st.button("Return from Laundry"):
        update_cloth_status(cloth_from_laundry, 'In Closet')
        st.success("Cloth returned from laundry!")

def get_laundry_clothes():
    st.subheader("Clothes in Laundry")
    clothes = get_clothes_by_status('In Laundry')
    
    for _, row in clothes.iterrows():
        st.image(row['image'], caption=row['name'])
        st.write(f"Name: {row['name']}")
        st.write("---")
