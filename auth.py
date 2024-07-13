import streamlit as st
import hashlib
import pandas as pd
from database import add_user, verify_user

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match")
        elif verify_user(username):
            st.error("Username already exists")
        else:
            hashed_password = hash_password(password)
            add_user(username, hashed_password)
            st.success("Registered successfully!")

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        hashed_password = hash_password(password)
        if verify_user(username, hashed_password):
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")
