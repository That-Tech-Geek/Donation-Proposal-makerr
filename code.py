import streamlit as st
from transformers import pipeline

# Initialize the chatbot
def create_chatbot():
    chatbot_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")
    return chatbot_pipeline

chatbot = create_chatbot()

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot(user_input)
    return response[0]['generated_text']

# Streamlit UI
st.title("Streamlit Chatbot")

# Input field for user message
user_message = st.text_input("You:")

# Display the chatbot response
if st.button("Send"):
    if user_message:
        with st.spinner("Thinking..."):
            response = get_response(user_message)
        st.text_area("Bot:", value=response, height=200, max_chars=None)
    else:
        st.error("Please enter a message.")
