import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Ensure pad_token_id is set to eos_token_id to avoid warnings
model.config.pad_token_id = model.config.eos_token_id

# Streamlit app
st.title("Customized Grant Donation Request Generator")

# Collect inputs from the user using Streamlit
donor_name = st.text_input("Enter name of donor:")
amount = st.number_input("Enter donation amount in USD:", min_value=1)
call_to_action = "We would love for you to visit our donation page or contact us directly to make this contribution."
project_details = st.text_area("Enter project details:", value="The Community Empowerment Initiative, which aims to provide essential resources and support to underprivileged communities.")
impact_statement = st.text_area("Enter impact statement:", value="empower these communities to become self-sustaining and improve the quality of life for countless individuals.")
personality_type = st.selectbox("Select donor psyche:", options=[
    "Analytical", "Emotional", "Visionary", "Pragmatic",
    "Creative", "Traditional", "Innovative", "Strategic",
    "Collaborative", "Detail-Oriented", "Big-Picture", "Ambitious",
    "Optimistic", "Realistic", "Caring", "Ethical",
    "Adventurous", "Discerning", "Methodical", "Inspirational",
    "Humble", "Assertive", "Passionate", "Reflective",
    "Open-Minded", "Dynamic", "Supportive"
])
organisation_name = st.text_input("Enter name of Organisation:")
poc_name = st.text_input("Enter name of Person of Contact:")
poc_position = st.text_input("Enter position of Point of Contact:")

# Function to generate a customized grant donation request based on donor personality
def generate_grant_request(donor_name, amount, call_to_action, project_details, impact_statement, personality_type, max_length=300):
    # Customize the prompt based on the personality type
    prompts = {
        "Analytical": (
            f"Dear {donor_name},\n\n"
            f"As someone who values data-driven decision-making, we wanted to share with you the measurable impact that a donation of ${amount} can have on our project, '{project_details}'. "
            f"Our research and projections indicate that with this contribution, we can {impact_statement}, ensuring that every dollar is put to optimal use.\n\n"
            f"{call_to_action}\n\n"
            f"We look forward to your support, knowing that your analytical approach will recognize the value of this investment.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Emotional": (
            f"Dear {donor_name},\n\n"
            f"We are reaching out to you because we know how deeply you care about making a difference in people's lives. With your heartfelt support, a donation of ${amount} to our project '{project_details}' "
            f"can bring hope and change to those who need it most. Imagine the joy and relief your generosity could bring.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for considering this opportunity to make a lasting impact on the lives of others.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Visionary": (
            f"Dear {donor_name},\n\n"
            f"You have always been a visionary, someone who sees the potential in every opportunity. We believe that with your support, a donation of ${amount} to our project '{project_details}' "
            f"could be the catalyst for transformative change. This project aligns with the future we both envision—a future where {impact_statement}.\n\n"
            f"{call_to_action}\n\n"
            f"Let’s create that future together.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Pragmatic": (
            f"Dear {donor_name},\n\n"
            f"We know you appreciate practical solutions that lead to tangible results. A donation of ${amount} to our project '{project_details}' "
            f"would directly contribute to achieving {impact_statement}. We’ve ensured that every dollar will be utilized effectively to maximize the impact.\n\n"
            f"{call_to_action}\n\n"
            f"Your pragmatic approach to philanthropy is exactly what we need to make this project a success.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Creative": (
            f"Dear {donor_name},\n\n"
            f"Your creativity and passion for new ideas inspire us. A donation of ${amount} to our project '{project_details}' could spark innovative solutions and unique approaches that transform the way we address our challenges. "
            f"Join us in bringing creative solutions to life and making a real difference.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your support and imaginative spirit.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Traditional": (
            f"Dear {donor_name},\n\n"
            f"Your dedication to preserving and valuing traditional approaches aligns perfectly with our mission. A donation of ${amount} to our project '{project_details}' will help maintain and enhance the classic methods we rely on. "
            f"Your support will ensure the continued success of tried-and-true solutions.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for keeping tradition alive with your generosity.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Innovative": (
            f"Dear {donor_name},\n\n"
            f"Your innovative thinking and forward-looking mindset are exactly what we need. A donation of ${amount} to our project '{project_details}' will support cutting-edge initiatives and breakthrough ideas that drive progress. "
            f"Help us push the boundaries and achieve remarkable results.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for embracing innovation with your support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Strategic": (
            f"Dear {donor_name},\n\n"
            f"Your strategic insight and planning are crucial to our success. A donation of ${amount} to our project '{project_details}' will help us execute our long-term goals and achieve significant milestones. "
            f"Your support will ensure that our strategy is effectively implemented.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your strategic thinking and support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Collaborative": (
            f"Dear {donor_name},\n\n"
            f"Your collaborative spirit and teamwork are vital to our mission. A donation of ${amount} to our project '{project_details}' will enhance our ability to work together and achieve collective goals. "
            f"Join us in creating positive change through cooperation and mutual support.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for fostering collaboration with your generosity.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Detail-Oriented": (
            f"Dear {donor_name},\n\n"
            f"Your attention to detail and thoroughness are greatly valued. A donation of ${amount} to our project '{project_details}' will ensure that every aspect is carefully managed and every resource is utilized effectively. "
            f"Your support will contribute to a meticulously executed project.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your meticulous approach and support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Big-Picture": (
            f"Dear {donor_name},\n\n"
            f"Your ability to see the big picture is inspiring. A donation of ${amount} to our project '{project_details}' will help us achieve significant long-term outcomes and make a substantial impact. "
            f"Your support will contribute to our overarching vision and goals.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your visionary perspective and support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Ambitious": (
            f"Dear {donor_name},\n\n"
            f"Your ambition and drive are just what we need. A donation of ${amount} to our project '{project_details}' will fuel our ambitious goals and help us reach new heights. "
            f"Your support will play a crucial role in achieving our lofty objectives.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your ambitious spirit and support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Optimistic": (
            f"Dear {donor_name},\n\n"
            f"Your optimism and positive outlook are incredibly motivating. A donation of ${amount} to our project '{project_details}' will help us maintain a hopeful and forward-looking approach. "
            f"Your support will contribute to creating a brighter future.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your optimistic support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Realistic": (
            f"Dear {donor_name},\n\n"
            f"Your realistic approach and practical mindset are essential to our success. A donation of ${amount} to our project '{project_details}' will ensure that we address practical needs and achieve feasible outcomes. "
            f"Your support will help us achieve realistic goals.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your practical support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Caring": (
            f"Dear {donor_name},\n\n"
            f"Your caring nature and compassion are truly appreciated. A donation of ${amount} to our project '{project_details}' will provide much-needed support and care to those in need. "
            f"Your generosity will make a significant difference in people's lives.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your caring support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Ethical": (
            f"Dear {donor_name},\n\n"
            f"Your commitment to ethical practices and integrity aligns perfectly with our values. A donation of ${amount} to our project '{project_details}' will support our efforts to uphold high ethical standards. "
            f"Your support will contribute to maintaining our commitment to ethical excellence.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your ethical support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Adventurous": (
            f"Dear {donor_name},\n\n"
            f"Your adventurous spirit and willingness to explore new opportunities are inspiring. A donation of ${amount} to our project '{project_details}' will help us undertake exciting new initiatives and ventures. "
            f"Your support will fuel our adventurous pursuits.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your adventurous support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Discerning": (
            f"Dear {donor_name},\n\n"
            f"Your discerning judgment and careful consideration are highly valued. A donation of ${amount} to our project '{project_details}' will help us ensure that every aspect is thoughtfully evaluated and effectively managed. "
            f"Your support will contribute to our discerning approach.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your discerning support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Methodical": (
            f"Dear {donor_name},\n\n"
            f"Your methodical approach and systematic mindset are essential to our success. A donation of ${amount} to our project '{project_details}' will help us implement processes and procedures effectively. "
            f"Your support will ensure a well-organized and efficient project execution.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your methodical support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Inspirational": (
            f"Dear {donor_name},\n\n"
            f"Your inspirational leadership and motivational energy are truly impactful. A donation of ${amount} to our project '{project_details}' will help us inspire others and drive positive change. "
            f"Your support will amplify our efforts to inspire and uplift those we serve.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your inspirational support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Humble": (
            f"Dear {donor_name},\n\n"
            f"Your humility and modesty are greatly appreciated. A donation of ${amount} to our project '{project_details}' will support our cause in a meaningful way, reflecting your unassuming generosity. "
            f"Your support will have a significant impact, all while staying true to your humble nature.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your humble support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Assertive": (
            f"Dear {donor_name},\n\n"
            f"Your assertive and proactive approach is highly valued. A donation of ${amount} to our project '{project_details}' will help us address key challenges and achieve our goals with determination. "
            f"Your support will empower us to take decisive actions and make an impact.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your assertive support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Passionate": (
            f"Dear {donor_name},\n\n"
            f"Your passion and enthusiasm for our cause are truly motivating. A donation of ${amount} to our project '{project_details}' will channel your energy into making a tangible difference. "
            f"Your support will fuel our passion and drive our efforts forward.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your passionate support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Reflective": (
            f"Dear {donor_name},\n\n"
            f"Your reflective nature and thoughtful consideration are greatly appreciated. A donation of ${amount} to our project '{project_details}' will help us make informed decisions and achieve our objectives. "
            f"Your support will contribute to a well-considered and impactful project.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your reflective support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Open-Minded": (
            f"Dear {donor_name},\n\n"
            f"Your open-mindedness and willingness to explore new ideas are highly valued. A donation of ${amount} to our project '{project_details}' will help us implement innovative solutions and embrace diverse perspectives. "
            f"Your support will foster an environment of openness and creativity.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your open-minded support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Dynamic": (
            f"Dear {donor_name},\n\n"
            f"Your dynamic and energetic approach to life is inspiring. A donation of ${amount} to our project '{project_details}' will help us maintain momentum and drive impactful change. "
            f"Your support will contribute to a vibrant and active project environment.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your dynamic support.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        ),
        "Supportive": (
            f"Dear {donor_name},\n\n"
            f"Your supportive and nurturing nature is greatly appreciated. A donation of ${amount} to our project '{project_details}' will provide the essential support and encouragement needed to succeed. "
            f"Your support will make a significant difference in achieving our goals.\n\n"
            f"{call_to_action}\n\n"
            f"Thank you for your supportive contribution.\n\n"
            f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
        )
    }
    
    prompt = prompts.get(personality_type, (
        f"Dear {donor_name},\n\n"
        f"We are writing to request your support for our project, '{project_details}'. With a donation of ${amount}, we can {impact_statement}. "
        f"Your contribution will make a significant difference.\n\n"
        f"{call_to_action}\n\n"
        f"Thank you for considering our request.\n\n"
        f"Sincerely,\n{poc_name}\n{poc_position}\n{organisation_name}"
    ))

    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate the text using the GPT-2 model
    output = model.generate(input_ids, max_length=500, num_return_sequences=1)
    
    # Decode the output
    letter = tokenizer.decode(output[0], skip_special_tokens=True)

    return letter
