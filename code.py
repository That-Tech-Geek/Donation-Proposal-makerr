import streamlit as st
from openai import OpenAI  # Import the OpenAI class

# Initialize OpenAI API using Streamlit secrets
api_key = st.secrets["openai"]["api_key"]
openai_client = OpenAI(api_key=api_key)

# Function to generate the custom pitch using the OpenAI API
def generate_pitch(name, cause, impact, personal_message):
    prompt = f"""
    Write a personalized donation pitch for a potential donor:

    Donor Name: {name}
    Cause: {cause}
    Impact: {impact}
    Personal Message: {personal_message}

    Pitch:
    """

    try:
        # Replace 'create_prompt_response' with the actual method for generating text
        response = openai_client.create_prompt_response(
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        # Adjust based on actual response structure
        pitch = response['choices'][0]['text'].strip()  
        return pitch
    except AttributeError as e:
        return f"An error occurred: {e} - Check if 'create_prompt_response' method exists."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

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
