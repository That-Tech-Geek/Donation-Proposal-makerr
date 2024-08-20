import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize the chatbot
def create_chatbot():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return tokenizer, model

tokenizer, model = create_chatbot()

# Function to get a response from the chatbot
def get_response(user_input):
    # Encode the new user input, add the EOS token, and return a tensor in PyTorch
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input tokens to the chat history
    bot_input_ids = new_user_input_ids

    # Generate a response using the model
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode the response and return it
    return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

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
