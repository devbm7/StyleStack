import streamlit as st
from clothes import add_cloth, update_cloth, delete_cloth, get_clothes_by_category
from laundry import send_to_laundry, return_from_laundry, get_laundry_clothes
from auth import login, register
from database import init_db
from notifications import notify_due_clothes
from analytics import display_analytics
from history import display_history

# Initialize database
init_db()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def main():
    st.title("Clothes and Laundry Management System")

    if not st.session_state['logged_in']:
        st.sidebar.subheader("Login/Register")
        auth_choice = st.sidebar.selectbox("Select Action", ["Login", "Register"])
        if auth_choice == "Login":
            login()
        else:
            register()
    else:
        st.sidebar.title("Menu")
        options = ["Add Cloth", "Update Cloth", "Delete Cloth", "View Clothes", "Manage Laundry", "Notifications", "Analytics", "History"]
        choice = st.sidebar.selectbox("Select Option", options)

        if choice == "Add Cloth":
            add_cloth()
        elif choice == "Update Cloth":
            update_cloth()
        elif choice == "Delete Cloth":
            delete_cloth()
        elif choice == "View Clothes":
            get_clothes_by_category()
        elif choice == "Manage Laundry":
            laundry_operations()
        elif choice == "Notifications":
            notify_due_clothes()
        elif choice == "Analytics":
            display_analytics()
        elif choice == "History":
            display_history()

def laundry_operations():
    st.subheader("Manage Laundry")
    action = st.selectbox("Action", ["Send to Laundry", "Return from Laundry", "View Laundry Clothes"])
    if action == "Send to Laundry":
        send_to_laundry()
    elif action == "Return from Laundry":
        return_from_laundry()
    elif action == "View Laundry Clothes":
        get_laundry_clothes()

if __name__ == "__main__":
    main()
