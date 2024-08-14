import streamlit as st
import openai

# Initialize OpenAI API (replace 'your-openai-api-key' with your actual OpenAI API key)
openai.api_key = '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'

# Function to generate the custom pitch using GPT-3
def generate_pitch(name, cause, impact, personal_message):
    prompt = f"""
    Write a personalized donation pitch for a potential donor:
    
    Donor Name: {name}
    Cause: {cause}
    Impact: {impact}
    Personal Message: {personal_message}
    
    Pitch:
    """
    
    # Call the OpenAI API to generate the pitch
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    pitch = response.choices[0].text.strip()
    return pitch

# Streamlit UI
st.title("Custom Donation Pitch Generator")

# Input fields for the donor information
name = st.text_input("Donor's Name", "")
cause = st.text_input("Cause", "")
impact = st.text_area("Describe the Impact", "")
personal_message = st.text_area("Add a Personal Message", "")

# Generate pitch when the button is clicked
if st.button("Generate Pitch"):
    if name and cause and impact and personal_message:
        pitch = generate_pitch(name, cause, impact, personal_message)
        st.subheader("Generated Pitch")
        st.write(pitch)
    else:
        st.error("Please fill in all fields before generating the pitch.")
