import streamlit as st
import gemini

# Initialize Gemini (gemini) API
gemini.api_key = 'AIzaSyB0PQ4LCaaSHa5H-3IKyoD0-9t8-YbFNcM'

# Function to generate a personalized pitch using the Gemini API
def generate_pitch(donor_name, bio, past_donations):
    prompt = f"""
    Create a personalized donation request pitch for the following donor:
    Name: {donor_name}
    Bio: {bio}
    Past Donations: ${past_donations}
    The pitch should be engaging, emphasize their interests, and encourage a donation.
    """
    response = gemini.Completion.create(
        model="gemini-1",  # Adjust the model name if necessary
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit Chatbot UI
st.title("Donation Pitch Chatbot")

st.write("This chatbot will help you generate a personalized donation request pitch based on the donor's information.")

# Initialize conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# User input for chatbot
user_input = st.text_input("You: ", key="input")

# Process user input and generate response
if st.button("Send"):
    if user_input:
        st.session_state.history.append(f"You: {user_input}")
        
        # Simple input processing
        if "name" in user_input.lower():
            donor_name = user_input.split(":")[1].strip()
            st.session_state.donor_name = donor_name
            st.session_state.history.append(f"Chatbot: Got it! The donor's name is {donor_name}. What about their bio?")
        
        elif "bio" in user_input.lower():
            donor_bio = user_input.split(":")[1].strip()
            st.session_state.donor_bio = donor_bio
            st.session_state.history.append(f"Chatbot: Thanks! I've noted that. How much have they donated in the past?")
        
        elif "donations" in user_input.lower():
            past_donations = user_input.split(":")[1].strip()
            st.session_state.past_donations = past_donations
            st.session_state.history.append(f"Chatbot: Perfect! Generating a personalized pitch for {st.session_state.donor_name}...")
            
            # Generate the donation pitch
            pitch = generate_pitch(st.session_state.donor_name, st.session_state.donor_bio, st.session_state.past_donations)
            st.session_state.history.append(f"Chatbot: Here's the pitch:\n\n{pitch}")
        
        else:
            st.session_state.history.append("Chatbot: Please provide the donor's name, bio, or donation amount.")

# Display the conversation history
for message in st.session_state.history:
    st.write(message)
