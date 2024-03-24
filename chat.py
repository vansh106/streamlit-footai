import streamlit as st
import requests
import os

def generate_response(prompt):
    local_server_url = "http://localhost:8080/post"  # Replace with your server's URL
    payload = {"prompt": prompt}

    try:
        response = requests.post(local_server_url, json=payload)
        response.raise_for_status()  # Handle errors
        return response.json()["response"]  # Assumes 'response' key in the JSON
    except requests.exceptions.RequestException as e:
        return "Sorry, server error occured."

st.title("Premier League Season 2023-24 Chatbot")
user_input = st.text_input("Talk to the chatbot:")

if st.button("Send"):
    if not user_input:
        st.warning("Please type a prompt.")
    else:
        with st.spinner("Thinking..."):
            bot_response = generate_response(user_input)
            st.write(bot_response)
