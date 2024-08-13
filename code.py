import streamlit as st
import gemini

# Initialize the API key
gemini.api_key = 'your-gemini-api-key'

# Function to generate a personalized pitch
def generate_pitch(donor_name, bio, past_donations):
    prompt = f"""
    Create a personalized donation request pitch for the following donor:
    Name: {donor_name}
    Bio: {bio}
    Past Donations: ${past_donations}
    The pitch should be engaging and encourage a donation.
    """
    response = gemini.Completion.create(
        model="gemini-1",  # Replace with the correct model name if needed
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Donation Pitch Chatbot")

st.write("This chatbot helps generate a personalized donation request pitch.")

# User input
donor_name = st.text_input("Donor Name")
donor_bio = st.text_area("Donor Bio")
past_donations = st.number_input("Past Donations (in USD)", min_value=0)

if st.button("Generate Pitch"):
    if donor_name and donor_bio:
        pitch = generate_pitch(donor_name, donor_bio, past_donations)
        st.subheader("Generated Donation Pitch:")
        st.write(pitch)
    else:
        st.warning("Please provide all required details.")
