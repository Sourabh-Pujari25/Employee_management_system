import streamlit as st
from utils import *
from pages.login import *
from streamlit_option_menu import option_menu
from statics.css_ui import *

st.set_page_config(layout="wide")



def main():
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
    project_dash()


def project_dash():
    if "project_name" not in st.session_state:
         st.session_state.project_name=""

    option_menu(menu_title=None,options=["Dashboard"],icons=["bi bi-window-fullscreen"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    
    
    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Add an expander in the first column
    with col1:
        with st.expander("Add Labour"):
            st.write("This is the content of Expander 1.")
            st.text_input("Input for Expander 1")

    # Add an expander in the second column
    with col2:
        with st.expander("Add New contractor"):
            st.write("This is the content of Expander 2.")
            st.slider("Slider for Expander 2", 0, 100)

    # Add an expander in the third column
    with col3:
        with st.expander("Add New Vendor"):
            st.write("This is the content of Expander 3.")
            st.selectbox("Select an option for Expander 3", ["Option 1", "Option 2", "Option 3"])
        
    with st.expander("Projects",expanded=True):
            projects = load_projects()
            create_project_space,projects_display=st.columns([3,7])
            with create_project_space:
                with st.container(border=True):
                    project_name = st.text_input("Create A New Project",label_visibility="collapsed")
                    if st.button("Create new Project",use_container_width=True):
                        if project_name:
                            # Check if the project already exists
                            if any(project['name'] == project_name for project in projects):
                                st.error(f"A project with the name '{project_name}' already exists.")
                            else:
                                new_project_id = get_next_project_id(projects)
                                new_project = {
                                    'id': new_project_id,
                                    'name': project_name,
                                    'new_work': [],
                                    'new_drawing':[]  # Placeholder for additional info
                                }
                                projects.append(new_project)
                                save_projects(projects)
                                st.success(f"Project '{project_name}' created with ID {new_project_id}.")
                    else:
                        st.error("Please enter a project name.")
            with projects_display:
                with open(JSON_FILE,'r') as f:
                    projects=f.read()
                projectnames=json.loads(projects)
                projectname_list=[]
                for project in projectnames:
                    projectname_list.append(project['name'])
                
                    
                num_rows = len(projectname_list) // 3
                num_cols = 3
                cols = st.columns(num_cols)
                project_name = None

                for i, folder_name in enumerate(projectname_list):
                    column_index = i % num_cols
                    column = cols[column_index]
                    with column:#
                        project_selected=st.button(folder_name,use_container_width=True,type="primary",key=folder_name)
                        if project_selected:
                            st.session_state.project_name= folder_name
                            st.switch_page("pages/dashboard.py")
                                                                    
            
            

            





if __name__=="__main__":
    main()