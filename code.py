import streamlit as st
import gemini
import pandas as pd

# Initialize Gemini (gemini) API
gemini.api_key = 'AIzaSyB0PQ4LCaaSHa5H-3IKyoD0-9t8-YbFNcM'

# Function to generate personalized pitch using Gemini API
def generate_pitch(donor_name, bio, past_donations):
    prompt = f"""
    Create a personalized donation request pitch for the following donor:
    Name: {donor_name}
    Bio: {bio}
    Past Donations: {past_donations}
    The pitch should be engaging, emphasize their interests, and encourage a donation.
    """
    response = gemini.Completion.create(
        model="gemini-1",  # Adjust the model name if necessary
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit UI
st.title("Personalized Donation Pitch Generator")

st.write("Enter the donor details to generate a customized donation request pitch.")

# User input for donor data
donor_name = st.text_input("Donor Name")
donor_bio = st.text_area("Donor Bio", "Enter a brief description or social media bio of the donor.")
past_donations = st.number_input("Past Donations (in USD)", min_value=0)

if st.button("Generate Pitch"):
    if donor_name and donor_bio:
        pitch = generate_pitch(donor_name, donor_bio, past_donations)
        st.subheader("Generated Donation Pitch:")
        st.write(pitch)
    else:
        st.warning("Please fill in all the fields to generate a pitch.")

# Display donor data if needed
if st.checkbox("Show Donor Data"):
    donor_data = load_data()  # Function to load existing donor data
    st.dataframe(donor_data)
