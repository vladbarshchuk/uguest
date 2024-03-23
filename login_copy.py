import streamlit as st
import sqlite3
import hashlib
import os
import json
import streamlit_authenticator as stauth
# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Define a function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user = []
# Create a login widget
def login_widget():
        # Check if the username and hashed password match the database
    users = cursor.execute("SELECT username FROM users").fetchall()
    passwords = cursor.execute("SELECT password FROM users").fetchall()
    #authenticator =stauth.Authenticate(username, hash_password(password), "UguestSession", "key1")
    #name, authenitaction_status, username = authenticator.login("Login","main")
    username=[]
    password=[]
    for x in users:
        username.append(x[0])
    for y in passwords:
        password.append(y[0])
    print(username, password)

    authenticator=stauth.Authenticate(username,password, "new", "random_key")
    

# Run the login widget
login_widget()

# Close the database connection
conn.close()