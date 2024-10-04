import streamlit as st
from utils import *
from pages.login import *
from streamlit_option_menu import option_menu
from statics.css_ui import *
from files.new_work import *


def dashboard():
    hide_pages()
    sidebar_colour()
    with st.sidebar:
        logo()
    if 'jwt_token' not in st.session_state or not st.session_state['logged_in']:
        st.error("You need to log in to access this page.")
        st.switch_page("pages/login.py")
    try:
        global decoded_token
        decoded_token = jwt.decode(st.session_state['jwt_token'], JWT_SECRET, algorithms=['HS256'])
        # st.write(decoded_token)
        st.sidebar.write(f"Welcome, {st.session_state['curr_userdetails'][1]}!")
    except jwt.ExpiredSignatureError:
        st.error("Session expired. Please log in again.")
        st.switch_page("pages/login.py")  # Redirect to login
    except jwt.InvalidTokenError:
        st.error("Invalid token. Please log in again.")
        st.switch_page("pages/login.py")
    dashboard_elements()



def dashboard_elements():
    select_project = st.sidebar.button("Select a Project",use_container_width=True)
    if select_project:
        st.switch_page("app.py")
    st.sidebar.markdown(
                """
                <div style="color: white; padding-bottom: 10px;">
                    Select User Action
                </div>
                """,
                unsafe_allow_html=True
            )
    dashboard_select=st.sidebar.radio("Select an option",options=["Add New Work","Labour Attendance","Add Drawing","Stock List"],label_visibility="collapsed")

    if dashboard_select=="Add New Work":
        new_work()
    elif dashboard_select=="Labour Attendance":
        try:
            lab_attendance()
        except FileNotFoundError:
            st.error("Please add Labour to the Project")

        # st.switch_page("pages/labour_attendance.py")
    elif dashboard_select=="Add Drawing":
        add_drawinng_fun()
    elif dashboard_select=="Stock List":
        stock_list_fun()



if __name__=="__main__":
    dashboard()