import streamlit as st
import json
import bcrypt
import jwt
from datetime import datetime, timedelta
import os
from statics.css_ui import *
from utils import *
import base64



def login_page():
    hide_pages()
    sidebar_colour()
    if "jwt_token" not in st.session_state:
        st.session_state['jwt_token']=None
    if "curr_userdetails" not in st.session_state:
        st.session_state['curr_userdetails']="" #
    
    # menu = ["Login", "Register"]
    # choice = st.sidebar.selectbox("Select an option", menu)
    space1,logo_space,space2=st.columns([20,70,20])
    with logo_space:
        with st.sidebar:
            logo() 
        st.markdown("""<center><h1 style="color: teal;">Sign in to Workspace</h1></center>""",unsafe_allow_html=True)
    with st.container(border=True):
        pad_left,content,pad_right=st.columns([10,80,10])
        with content:
            st.markdown("""<div style="height: 20px;"></div>""",unsafe_allow_html=True)
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            login_button=st.button("Login",use_container_width=True,type="primary")
            st.markdown("""<div style="height: 20px;"></div>""",unsafe_allow_html=True)
        
        
        if login_button:
            user_data = load_user_data()
            # st.write(user_data)
            # try:
            for i in user_data:
                if username == i['email'] and verify_password(i['password'], password):
            
                    st.session_state['jwt_token'] = create_jwt_token(username)
                    st.session_state['logged_in'] = True
                    st.success(f"Login successful!")
                    st.session_state['curr_userdetails']=(i['email'],i['name'])
                    st.switch_page("app.py")
                else:
                    st.error("Invalid username or password.")
            # except:
            #     st.error("Please Enter Valid Details")
 
if __name__=="__main__":
    login_page() 


 # if choice == "Register":
    #     st.subheader("Register")
    #     username = st.text_input("Username")
    #     password = st.text_input("Password", type='password')
    #     if st.button("Register"):
    #         if username and password:
    #             user_data = load_user_data()
    #             if username in user_data:
    #                 st.error("Username already exists!")
    #             else:
    #                 hashed_password = hash_password(password)
    #                 user_data[username] = hashed_password
    #                 save_user_data(user_data)
    #                 st.success("Registration successful!")
    #         else:
    #             st.error("Please enter both username and password.")

    # elif choice == "Login":