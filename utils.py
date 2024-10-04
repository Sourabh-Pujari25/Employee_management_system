import json
import bcrypt
from datetime import datetime, timedelta
import os
import streamlit as st
import jwt



JSON_FILE = 'database/projects.json'
JWT_SECRET = "qwertyuiop12345676qwertyuasdfgh"  # Change this to a random secret key
JWT_ALGORITHM = "HS256"
JWT_EXP_DELTA_SECONDS = 3600  # Token expiry time in seconds
USER_DATA_FILE = "database/user_data.json"



# Helper functions
def load_user_data():
    try:
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(data, f,indent=4)

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

def create_jwt_token(username):
    payload = {
        'sub': username,
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def get_user_type(user):
    users=load_user_data()
    
    for i in users:
        st.write(i)
        if isinstance(i, dict) and i['adminUser'] == user:
            return i['userType']
    return None



###########projects

def load_projects():
    # Check if the JSON file exists
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    # If not, create an empty list
    return []

# Function to save projects to the JSON file
def save_projects(projects):
    with open(JSON_FILE, 'w') as f:
        json.dump(projects, f, indent=4)

# Function to generate the next project ID
def get_next_project_id(projects):
    if not projects:
        return "PJ_001"
    else:
        last_project = projects[-1]
        last_id = last_project['id']
        last_num = int(last_id.split('_')[1])
        next_num = last_num + 1
        return f"PJ_{next_num:03}"