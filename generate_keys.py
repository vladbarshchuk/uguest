import pickle 
from pathlib import Path

import streamlit_authenticator as stauth

names = ['Peter Parker', 'Robert Tzes']
username = ['pparker', 'rtzes']
passwords = ['hoboken1', 'js123!']

hashed_passwords=stauth.Hasher(passwords).generate()

file_path =Path(__file__).present /'hashed_pw.pkl'
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)