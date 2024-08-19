import streamlit as st
from google.cloud import dialogflow_v2 as dialogflow
from google.oauth2 import service_account

# Initialize Dialogflow client using Streamlit secrets
credentials = service_account.Credentials.from_service_account_info(st.secrets["dialogflow_credentials"])
client = dialogflow.SessionsClient(credentials=credentials)
project_id = st.secrets["dialogflow_project_id"]

# Function to generate the custom pitch using Dialogflow API
def generate_pitch(name, cause, impact, personal_message):
    session_id = "unique-session-id"  # You can generate a unique session ID if needed
    session = client.session_path(project_id, session_id)

    prompt = f"""
    Write a personalized donation pitch for a potential donor:

    Donor Name: {name}
    Cause: {cause}
    Impact: {impact}
    Personal Message: {personal_message}

    Pitch:
    """

    text_input = dialogflow.TextInput(text=prompt, language_code='en')
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = client.detect_intent(session=session, query_input=query_input)
        pitch = response.query_result.fulfillment_text.strip()
        return pitch
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("Custom Donation Pitch Generator")

# Input fields for the donor information
name = st.text_input("Donor's Name")
cause = st.text_input("Cause")
impact = st.text_area("Describe the Impact")
personal_message = st.text_area("Add a Personal Message")

# Generate pitch when the button is clicked
if st.button("Generate Pitch"):
    if name and cause and impact and personal_message:
        with st.spinner("Generating your custom pitch..."):
            pitch = generate_pitch(name, cause, impact, personal_message)
        st.subheader("Generated Pitch")
        st.write(pitch)
    else:
        st.error("Please fill in all fields before generating the pitch.")
