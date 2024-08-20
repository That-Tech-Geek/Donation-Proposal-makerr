import streamlit as st
import requests

# Streamlit UI
st.title("Streamlit Chatbot with Rasa")

# Input field for user message
user_message = st.text_input("You:")

# Function to get a response from Rasa
def get_response(user_input):
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"message": user_input}
    )
    response_json = response.json()
    return response_json[0]['text'] if response_json else "No response"

# Display the chatbot response
if st.button("Send"):
    if user_message:
        with st.spinner("Thinking..."):
            response = get_response(user_message)
        st.text_area("Bot:", value=response, height=200, max_chars=None)
    else:
        st.error("Please enter a message.")
