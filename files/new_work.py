import streamlit as st
from utils import *
from pages.login import *
from streamlit_option_menu import option_menu
from statics.css_ui import *

def new_work():
    option_menu(menu_title=None,options=["Add New Work 🏗️"],icons=["bi bi-cone-striped"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    with st.container(border=True):
        # df_work=all_works()
        # st.data_editor(df_work,use_container_width=True)

        work_name_col,work_date_col=st.columns([2,2])
        with work_name_col:
            st.session_state.work_name = st.text_input("Enter Work Name")
        with work_date_col:
            st.session_state.work_date = st.date_input("Select Date")
    st.session_state.add_work_butt = False
    option_menu(menu_title=None,options=["Work Details"],key="title",icons=["bi bi-pencil"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    
    with st.container(border=True):
        st.subheader("Step 1: Add Material Details")
        col1,col2=st.columns([4,1])
    
        with col1:
                st.session_state.vard_material=st.selectbox("Vardhaman Material",options=["Option 1","Option 2","Option 3"]) #QTY with this
                st.session_state.mcc_material=st.text_input("MCC Material",key="mcc")# QTY with this
        with col2:
            st.session_state.vard_material_qty = st.number_input("Select Quantity",min_value=1)
            st.session_state.mcc_material_qty = st.number_input("Select Quantity",key="mcc_qty",min_value=1)
        col_1,col_2,col_3=st.columns([1,1,1])

    option_menu(menu_title=None,options=["Excavation Details"],key="title_excavation",icons=["bi bi-pencil"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    with st.container(border=True):
        col1,col2=st.columns([1,2])
    
        with col1:
            st.session_state.excavation_material=st.selectbox("Excavation Material",key="excavation__material",options=["Option 1","Option 2","Option 3"]) 
            st.session_state.excavation_len=st.number_input("Length",min_value=0.1,placeholder="m",key="exc_len")
            st.session_state.excavation_width=st.number_input("Width",min_value=0.1,placeholder="m",key="exc_width")
            st.session_state.excavation_depth=st.number_input("Depth",min_value=0.94,placeholder="m",key="exc_depth")
            with st.container(border=True):
                st.subheader("Dewatering")
                st.session_state.dewatering_inp = st.number_input("Select Quantity",key="dewatering_inp__",min_value=1)
            
            
    # QTY with this
        with col2:
            with st.container(border=True):
                st.subheader("JCB Bucket Details")
                st.session_state.jcb_bucket_start_time=st.time_input("Start Time",value="now")
                st.session_state.jcb_start_photo = st.file_uploader("Upload Start Time Photo")
                st.session_state.jcb_bucket_end_time=st.time_input("End Time",value="now")
                st.session_state.jcb_end_photo = st.file_uploader("Upload End Time Photo")
                with st.expander("JCB Breaker Details"):
                    st.subheader("JCB Breaker Details")
                    st.session_state.jcb_breaker_start_time=st.time_input("Start Time",value="now",key="breaker 01")
                    st.session_state.jcb_breaker_start_photo = st.file_uploader("Upload Start Time Photo",key="breaker 02")
                    st.session_state.jcb_breaker_bucket_end_time=st.time_input("End Time",value="now",key="breaker 03")
                    st.session_state.jcb_breaker_end_photo = st.file_uploader("Upload End Time Photo",key="breaker 04")

    option_menu(menu_title=None,options=["Additional Details"],key="title_excavation_",icons=["bi bi-pencil"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "white"},})
    with st.container(border=True):
        st.session_state.site_pic = st.file_uploader("Upload Site Photos",accept_multiple_files=True)
        st.session_state.drawing_pic = st.file_uploader("Upload Drawing Documents",accept_multiple_files=True)
        st.session_state.select_labours=st.multiselect("Select labours",options=["Option 1","Option 2","Option 3"])

        #notes
        st.session_state.notes = st.text_area("Add Additional Notes",height=200)
        add_cols=st.columns([1,2,1])
        with add_cols[1]:
            submit_works=st.button("Save & Submit",use_container_width=True,type="primary")
    
    if submit_works:
        # work_id = get_next_work_id()
        work_data = {
            'Name of Work': st.session_state.work_name,
            'Date': str(st.session_state.work_date),
            'Vardhaman Material': {'items': st.session_state.vard_material, 'quantity': st.session_state.vard_material_qty},
            'MMC Material': {'items': st.session_state.mcc_material, 'quantity': st.session_state.mcc_material_qty},
            'Excavation': {
                'Length': st.session_state.excavation_len,
                'Width': st.session_state.excavation_width,
                'Depth': st.session_state.excavation_depth,
                'Material': st.session_state.excavation_material,
            },
            'JCB Bucket': {
                'Start Time': str(st.session_state.jcb_bucket_start_time),
                'Stop Time': str(st.session_state.jcb_bucket_end_time),
                'Start Photo': st.session_state.jcb_start_photo.name if st.session_state.jcb_start_photo else None,
                'Stop Photo': st.session_state.jcb_end_photo.name if st.session_state.jcb_end_photo else None
            },
            'JCB Breaker': {
                'Start Time': str(st.session_state.jcb_breaker_start_time),
                'Stop Time':  str(st.session_state.jcb_breaker_bucket_end_time),
                'Start Photo': st.session_state.jcb_breaker_start_photo.name if st.session_state.jcb_breaker_start_photo else None,
                'Stop Photo': st.session_state.jcb_breaker_end_photo.name if st.session_state.jcb_breaker_end_photo else None
            },
            'Dewatering': st.session_state.dewatering_inp,
            'Site Photos': [file.name for file in st.session_state.site_pic] if st.session_state.site_pic else [],
            'Drawing Upload': [file.name for file in st.session_state.drawing_pic] if st.session_state.drawing_pic else [],
            'Labour': st.session_state.select_labours,
            'Additional Notes': st.session_state.notes
        }

        filename = JSON_FILE
        append_work_data_to_json(filename, st.session_state.project_name, work_data)

        

        st.success('Work details saved successfully!')
    
def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    data_dict = eval(content)
    return data_dict

def get_next_work_id():
    """Generate the next Work ID based on the latest entry in the JSON file."""
    file_path = JSON_FILE
    if not os.path.exists(file_path):
        return 'WID_001'

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        return 'WID_001'

    if not data:
        return 'WID_001'

    # Extract the latest Work ID
    try:
        latest_id = max(item['Work ID'] for item in data)
        number = int(latest_id.split('_')[1])
        new_number = number + 1
        return f'WID_{new_number:03}'
    except KeyError:
        return 'WID_001'

def load_existing_data():
    """Load existing work data from JSON file."""
    file_path = f'{st.session_state.work_data_save_path}/work_data.json'
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []



def add_new_material():

    # Streamlit form
    with st.form(key='add_material_form'):
        material_type = st.selectbox("Select Material Type", ("Vardhaman Material", "MCC Material"))
        # Material Name
        material_name = st.text_input("Material Name")
        # Material Description
        material_data = st.date_input("Material Date")
        material_size = st.text_input("Material Size")
        godown_name = st.text_input("Godown Name")
        vendor_name = st.text_input("Vendor Name")
        # Submit button
        col_1,col_2,col_3=st.columns([1,2,1])
        with col_2:
            submit_button = st.form_submit_button(label="Add Material",use_container_width=True,type="primary")
        # Handling form submission
        if submit_button:
            pass

def add_contractor():
    with st.container(border=True):
        contractor_name = st.selectbox("Select Material Type", ("Vardhaman Material", "MCC Material"))


    
# Function to load existing data from the JSON file
def load_data(json_file_path):
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save data to the JSON file
def save_data(data,json_file_path):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)



def append_work_data_to_json(filename, name, work_data):
    # Load existing JSON data
    with open(filename, 'r') as file:
        json_data = json.load(file)

    # Find the entry for the given name
    for entry in json_data:
        if entry['name'] == name:
            # Determine the next incremental ID
            current_count = len(entry['new_work'])
            if current_count == 0:
                new_id = 'WID_001'
            else:
                # Incremental ID logic
                last_id = entry['new_work'][-1]['Work ID']
                number = int(last_id.split('_')[1]) + 1
                new_id = f'WID_{number:03}'

            # Prepare new entry with generated ID
            new_entry = {
                'Work ID': new_id,
                **work_data  # Unpack work_data into the new entry
            }
            entry['new_work'].append(new_entry)
            break

    # Save the updated JSON data back to the file
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=4)


if __name__=="__main__":
    new_work()






# i have this json 

# work_data = {
#             'Work ID': work_id,
#             'Name of Work': st.session_state.work_name,
#             'Date': str(st.session_state.work_date),
#             'Vardhaman Material': {'items': st.session_state.vard_material, 'quantity': st.session_state.vard_material_qty},
#             'MMC Material': {'items': st.session_state.mcc_material, 'quantity': st.session_state.mcc_material_qty},
#             'Excavation': {
#                 'Length': st.session_state.excavation_len,
#                 'Width': st.session_state.excavation_width,
#                 'Depth': st.session_state.excavation_depth,
#                 'Material': st.session_state.excavation_material,
#             },
#             'JCB Bucket': {
#                 'Start Time': str(st.session_state.jcb_bucket_start_time),
#                 'Stop Time': str(st.session_state.jcb_bucket_end_time),
#                 'Start Photo': st.session_state.jcb_start_photo.name if st.session_state.jcb_start_photo else None,
#                 'Stop Photo': st.session_state.jcb_end_photo.name if st.session_state.jcb_end_photo else None
#             },
#             'JCB Breaker': {
#                 'Start Time': str(st.session_state.jcb_breaker_start_time),
#                 'Stop Time':  str(st.session_state.jcb_breaker_bucket_end_time),
#                 'Start Photo': st.session_state.jcb_breaker_start_photo.name if st.session_state.jcb_breaker_start_photo else None,
#                 'Stop Photo': st.session_state.jcb_breaker_end_photo.name if st.session_state.jcb_breaker_end_photo else None
#             },
#             'Dewatering': st.session_state.dewatering_inp,
#             'Site Photos': [file.name for file in st.session_state.site_pic] if st.session_state.site_pic else [],
#             'Drawing Upload': [file.name for file in st.session_state.drawing_pic] if st.session_state.drawing_pic else [],
#             'Labour': st.session_state.select_labours,
#             'Additional Notes': st.session_state.notes
#         }


# and i have a json file 
# which has data 
# [
#     {
#         "id": "PJ_001",
#         "name": "Sourabh",
#         "additional_info": {}
#     },
#     {
#         "id": "PJ_002",
#         "name": "Sourabhws",
#         "additional_info": {}
#     }
# ]


# i want to append work_data for the given "name" in the file in the additional information section and as i will append the new work_datta i want to append it without over writing it 