import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to generate a simple response using spaCy
def generate_response(user_input):
    doc = nlp(user_input)
    entities = set()

    # Extract named entities from the input
    for ent in doc.ents:
        entities.add(ent.text)

    if entities:
        return f"Interesting! You mentioned: {', '.join(entities)}"
    else:
        return "Sorry, I didn't quite understand that."

# Streamlit UI
st.title("Streamlit Chatbot with spaCy")

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
