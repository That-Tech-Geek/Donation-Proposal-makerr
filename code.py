import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize the chatbot
def create_chatbot():
    bot = ChatBot("StreamlitBot", logic_adapters=["chatterbot.logic.BestMatch"])
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train("chatterbot.corpus.english")  # Train the bot with the English corpus
    return bot

chatbot = create_chatbot()

# Function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

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
