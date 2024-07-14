import streamlit as st
from database import get_laundry_due
import datetime

def notify_due_clothes():
    st.subheader("Notifications")
    due_clothes = get_laundry_due()
    current_time = datetime.datetime.now()
    
    for _, row in due_clothes.iterrows():
        last_action_time = datetime.datetime.strptime(row['last_action_time'], '%Y-%m-%d %H:%M:%S')
        days_due = (current_time - last_action_time).days
        if days_due > 2:
            st.write(f"Cloth '{row['name']}' has been in the laundry for {days_due} days.")
