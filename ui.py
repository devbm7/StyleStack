import streamlit as st

def display_images(clothes):
    st.subheader("Clothes")
    cols = st.columns(3)
    for idx, row in clothes.iterrows():
        with cols[idx % 3]:
            st.image(row['image'], caption=row['name'])
            st.write(f"Category: {row['category']}")
            st.write(f"Status: {row['status']}")
