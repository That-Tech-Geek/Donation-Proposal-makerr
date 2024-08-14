import streamlit as st
import openai  # Import the openai module

# Initialize OpenAI API using Streamlit secrets
api_key = st.secrets["openai_api_key"]
openai.api_key = api_key  # Set the API key

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
        # Use the OpenAI API call to generate the pitch
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )
        pitch = response.choices[0].message.content.strip()
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
