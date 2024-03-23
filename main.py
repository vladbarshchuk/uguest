import streamlit as st
import sqlite3
#import openai_key
import time
import json
import os
import keyboard
with open('list.json', 'r') as file:
    # Load the JSON data from the file
    json_data = json.load(file)
print(json_data)
st.title("UGuest")
with st.sidebar:
    option = st.selectbox(
    'Please Choos Your Hotel',
    ('The Roxy Hotel New York', 'Moxy Brooklyn Williamsburg'), 
    index=None,
   placeholder="Hotel Name")
    if st.button("Logout"):
        # Clear the JSON file
        with open('list.json', 'w') as file:
            file.write(json.dumps([]))
        st.success("Logout successful!")
        keyboard.press_and_release('command+w')
        os.system('streamlit run login.py')
st.write('You selected:', option)




prompt = st.chat_input("What can I help you with ?")
if prompt=="Hey":
    with st.chat_message("assistant", avatar='🤖'):
        st.write("Hey Vlad ! What can I help you with?")
elif prompt=="When is my airport shuttle tomorrow ?":
    with st.chat_message("assistant", avatar='🤖'):
        st.write(f"Your {option} shuttle will be waiting for you at 8:00 am.")
elif prompt=="Could you change it to 10 am?":
    with st.chat_message("assistant", avatar='🤖'):
        st.write(f"Your shuttle time has been changed successfully 👍! \n\nYour {option} shuttle will be waiting for you at 10:00 am.")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
