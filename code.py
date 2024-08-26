import streamlit as st
import requests

# Define the Rasa API endpoint using Streamlit secrets
RASA_API_URL = st.secrets["rasa_url"]

# Function to interact with Rasa and get a response
def get_rasa_response(message):
    response = requests.post(RASA_API_URL, json={"message": message})
    if response.status_code == 200:
        response_json = response.json()
        if response_json:
            return response_json[0]['text']
    return "Sorry, I couldn't generate a response."

# Streamlit app layout
st.title("Grant Donation Request Generator")

# User inputs
donor_name = st.text_input("Enter the name of the donor:")
amount = st.number_input("Enter donation amount in USD:", min_value=0)
call_to_action = st.text_input("Enter call to action:")
project_details = st.text_input("Enter project details:")
impact_statement = st.text_input("Enter impact statement:")
personality_type = st.selectbox("Select donor personality type:", [
    "Analytical", "Emotional", "Visionary", "Pragmatic", "Charismatic", 
    "Generous", "Innovative", "Strategic", "Compassionate", "Resourceful", 
    "Leadership", "Collaborative", "Philanthropic", "Entrepreneurial", 
    "Committed"
])
organisation_name = st.text_input("Enter the name of your organisation:")
poc_name = st.text_input("Enter the name of the person of contact:")
poc_position = st.text_input("Enter the position of the point of contact:")

# Generate the message
if st.button("Generate Grant Request"):
    if all([donor_name, amount, call_to_action, project_details, impact_statement, 
            personality_type, organisation_name, poc_name, poc_position]):
        
        # Construct the message for Rasa
        message = (
            f"Generate a grant donation request for a donor named {donor_name} who is "
            f"{personality_type}. The donation amount is ${amount}. The call to action is "
            f"'{call_to_action}'. The project details are '{project_details}', and the impact statement is "
            f"'{impact_statement}'. The organisation name is {organisation_name}. The point of contact is "
            f"{poc_name} who holds the position of {poc_position}."
        )
        
        # Get the response from Rasa
        response_text = get_rasa_response(message)
        
        # Display the response
        st.subheader("Generated Grant Request")
        st.write(response_text)
    else:
        st.error("Please fill in all the fields.")
