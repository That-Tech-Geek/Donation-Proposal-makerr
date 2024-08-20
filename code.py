import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello', ['Hello!', 'Hi there!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am great, thanks for asking!']),
    (r'what is your name?', ['I am a chatbot created by NLTK.', 'You can call me NLTK Bot.']),
    (r'quit', ['Bye! Take care.']),
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.respond(user_input)
    return response if response else "Sorry, I didn't understand that."

# Streamlit UI
st.title("Streamlit Chatbot with NLTK")

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
