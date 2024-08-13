import streamlit as st
import requests

# Function to generate a personalized pitch using the LLaMA API
def generate_pitch(donor_name, bio, past_donations):
    api_url = "LL-ATLBeF16yEleBb6RmOf9g4uGeN4GOUAqbJXY1RuKpSC4x62ABkeigtFVo01o5m0o"  # Replace with the actual LLaMA API URL
    api_key = "api.llama.ai/"  # Replace with your actual LLaMA API key
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": f"""
        Create a personalized donation request pitch for the following donor:
        Name: {donor_name}
        Bio: {bio}
        Past Donations: ${past_donations}
        The pitch should be engaging and encourage a donation.
        """,
        "max_tokens": 150
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["text"].strip()

# Streamlit UI
st.title("Donation Pitch Chatbot")

st.write("This chatbot helps generate a personalized donation request pitch.")

# User input
donor_name = st.text_input("Donor Name")
donor_bio = st.text_area("Donor Bio")
past_donations = st.number_input("Past Donations (in USD)", min_value=0)

if st.button("Generate Pitch"):
    if donor_name and donor_bio:
        try:
            pitch = generate_pitch(donor_name, donor_bio, past_donations)
            st.subheader("Generated Donation Pitch:")
            st.write(pitch)
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide all required details.")
