import streamlit as st
import json
import os
import re
from utils import *

# Define the path to your JSON file
json_file_path = 'database/user_data.json'

# Function to read existing data from the JSON file
def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            if content:  # If the file is not empty
                return json.loads(content)
            else:
                return []  # Return an empty list if the file is empty
    return []  # Return an empty list if file doesn't exist

# Function to ensure the JSON file exists
def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)  # Create an empty JSON array

# Ensure the file exists at the beginning of the script
ensure_file_exists(json_file_path)

# Function to write updated data to the JSON file
def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Function to generate the next ID
def generate_next_id(existing_data):
    if not existing_data:
        return 'US_001'
    
    # Extract current IDs and find the maximum
    ids = [entry['id'] for entry in existing_data]
    max_id = max(ids, key=lambda x: int(re.search(r'\d+', x).group()))
    next_id_number = int(re.search(r'\d+', max_id).group()) + 1
    
    return f'US_{next_id_number:03}'

# Create a form for user input
with st.form(key='data_form'):
    name = st.text_input('Enter your name')
    email = st.text_input('Enter your email')
    password = st.text_input('Enter your Password',key="passs",type="password")
    adminpass= hash_password(password)
    UserType = st.selectbox('Select User Type', options=["Super User", "Admin", "Member"])
    submit_button_reg = st.form_submit_button(label='Register')

    if submit_button_reg:
        # Read existing data
        existing_data = read_json(json_file_path)

        # Check if the email already exists
        if any(entry['email'] == email for entry in existing_data):
            st.error('This email is already registered. Please use a different email.')
        else:
            # Generate a new ID
            new_id = generate_next_id(existing_data)

            # Create a new entry
            new_entry = {
                'id': new_id,
                'name': name,
                'email': email,
                'UserType': UserType,
                'password':adminpass,
            }

            # Append the new entry to existing data
            existing_data.append(new_entry)

            # Write the updated data back to the JSON file
            write_json(json_file_path, existing_data)

            # Confirm submission
            st.success(f'Data saved successfully with ID: {new_id}')
