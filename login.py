import streamlit as st
import sqlite3
import hashlib
import os
import json
# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Define a function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user = []
# Create a login widget
def login_widget():

    st.title("Login")
    username = st.text_input("Username",key="unique")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
            # Check if the username and hashed password match the database
            cursor.execute("SELECT username, password FROM users WHERE username=?", (username,))
            result = cursor.fetchone()

            if result:
                db_username, db_hashed_password = result
                if db_hashed_password == hash_password(password):
                    
                    st.success("Login successful!")
                    user.append(db_username)
                    json_data = json.dumps(user)
                    with open('list.json', 'w') as file:
                        file.write(json_data)
                    
                    os.system('streamlit run main.py')
                    
                else:
                    st.error("Incorrect password")
                    print(db_hashed_password, hash_password(password))
            else:
                st.error("User not found")


# Run the login widget
login_widget()

# Close the database connection
conn.close()