import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download required NLTK data files (do this once)
nltk.download('punkt')
nltk.download('wordnet')

# Function to generate a simple response
def generate_response(user_input):
    tokens = word_tokenize(user_input.lower())
    synonyms = set()

    # Find synonyms for each token
    for token in tokens:
        for syn in wordnet.synsets(token):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())

    if synonyms:
        return f"Interesting! You mentioned: {', '.join(synonyms)}"
    else:
        return "Sorry, I didn't quite understand that."

# Streamlit UI
st.title("Streamlit Chatbot with NLTK")

# Input field for user message
user_message = st.text_input("You:")

# Display the chatbot response
if st.button("Send"):
    if user_message:
        with st.spinner("Thinking..."):
            response = generate_response(user_message)
        st.text_area("Bot:", value=response, height=200, max_chars=None)
    else:
        st.error("Please enter a message.")
