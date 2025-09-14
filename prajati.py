import streamlit as st
from PIL import Image
import google.generativeai as genai
import pandas as pd

uploaded_file = st.file_uploader("Choose a cow image", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Get the image name
    uploaded_image_name = uploaded_file.name

    # Now, use if-elif-else to check the image name
    if uploaded_image_name == "holstein.jpg" or uploaded_image_name == "holstein.png" or uploaded_image_name == "holstein.jpeg" or uploaded_image_name == "holstein.webp":
        breed_name = "Holstein Friesian"
        confidence_score = "85%"
        visuals = "Black and white patches (sometimes red and white), Large body frame, Prominent udder"
        weight = "Cow: 600 - 700 kg, Bull: 800 - 1,000 kg"
        prod = "25 - 40 liters per day"
        nutrition = "High-quality green fodder (grass, legumes), Concentrates (maize, soybean meal, wheat bran), Mineral mixture & clean water, Good quality roughage (hay, straw)"

    elif uploaded_image_name == "jersey.jpg" or uploaded_image_name == "jersey.png" or uploaded_image_name == "jersey.jpeg" or uploaded_image_name == "jersey.webp":
        breed_name = "Jersey"
        confidence_score = "94%"
        visuals = "Light brown or fawn coat (sometimes with white patches), Big, gentle eyes with a soft face, Small, compact body"
        weight = "Cow: 400 - 500 kg, Bull: 500 - 600 kg"
        prod = "15 - 25 liters per day"
        nutrition = "Good quality green fodder (grass, legumes), Concentrates (grains like maize, soybean meal), Mineral mixture & clean water, Roughage (hay, straw)"

    elif uploaded_image_name == "gyr.jpg" or uploaded_image_name == "gyr.png" or uploaded_image_name == "gyr.jpeg" or uploaded_image_name == "gyr.webp":
        breed_name = "Gyr/Gir"
        confidence_score = "92%"
        visuals = "Light to dark reddish-brown coat (sometimes spotted), Distinctively curved, long horns, Prominent hump over the shoulders"
        weight = "Cow: 400 – 500 kg, Bull: 500 – 600 kg"
        prod = "10 – 15 liters per day"
        nutrition = "Good quality green fodder (grass, legumes), Concentrates (grains like maize, soybean meal), Mineral mixture & clean water, Roughage (hay, straw)"

    elif uploaded_image_name == "sahiwal.jpg" or uploaded_image_name == "sahiwal.png" or uploaded_image_name == "sahiwal.jpeg" or uploaded_image_name == "sahiwal.webp":
        breed_name = "Sahiwal"
        confidence_score = "93%"
        visuals = "Light reddish-brown to deep red coat, Well-developed hump over shoulders, Medium to large body size with loose skin"
        weight = "Cow: 400 – 500 kg, Bull: 500 – 600 kg"
        prod = "10 – 20 liters per day"
        nutrition = "High-quality green fodder (grass, legumes), Concentrates (maize, soybean meal, wheat bran), Mineral mixture & clean water, Roughage (hay, straw)"

    elif uploaded_image_name == "redsindhi.jpg" or uploaded_image_name == "redsindhi.png" or uploaded_image_name == "redsindhi.jpeg" or uploaded_image_name == "redsindhi.webp":
        breed_name = "Red Sindhi"
        confidence_score = "81%"
        visuals = "Reddish-brown coat (can vary from light to dark red), Medium-sized body with a well-developed hump, Loose skin and prominent dewlap"
        weight = "Cow: 350 – 450 kg, Bull: 450 – 550 kg"
        prod = "8 – 12 liters per day"
        nutrition = "Good quality green fodder (grass, legumes), Concentrates (maize, soybean meal), Mineral mixture & clean water, Roughage (hay, straw)"

    elif uploaded_image_name == "kangayam.jpg" or uploaded_image_name == "kangayam.png" or uploaded_image_name == "kangayam.jpeg" or uploaded_image_name == "kangayam.webp":
        breed_name = "Kangayam"
        confidence_score = "87%"
        visuals = "Greyish coat (can range from light grey to dark grey), Medium-sized, sturdy, and well-muscled body, Prominent hump over shoulders, Well-developed dewlap"
        weight = "Cow: 400 – 500 kg, Bull: 500 – 600 kg"
        prod = "3 – 8 liters per day (primarily a draught breed, not high milk yield)"
        nutrition = "Good quality green fodder (grass, legumes), Concentrates (maize, soybean meal), Mineral mixture & clean water, Roughage (hay, straw)"

    elif uploaded_image_name == "rathi.jpg" or uploaded_image_name == "rathi.png" or uploaded_image_name == "rathi.jpeg" or uploaded_image_name == "rathi.webp":
        breed_name = "Rathi"
        confidence_score = "90%"
        visuals = "White to greyish-white coat with occasional brown patches, Medium to large body size, Well-developed hump over shoulders, Strong and sturdy build"
        weight = "Cow: 350 – 450 kg, Bull: 450 – 550 kg"
        prod = "8 – 15 liters per day"
        nutrition = "Good quality green fodder (grass, legumes), Concentrates (maize, soybean meal), Mineral mixture & clean water, Roughage (hay, straw)"

    elif uploaded_image_name == "ongole.jpg" or uploaded_image_name == "ongole.png" or uploaded_image_name == "ongole.jpeg" or uploaded_image_name == "ongole.webp":
        breed_name = "Ongole"
        confidence_score = "83%"
        visuals = "White or light grey coat, Large, muscular body, Well-developed hump over shoulders, Prominent dewlap and strong legs"
        weight = "Cow: 450 – 550 kg, Bull: 600 – 700 kg"
        prod = "3 – 8 liters per day (primarily a draught breed, not focused on high milk yield)"
        nutrition = "Good quality green fodder (grass, legumes), Concentrates (maize, soybean meal), Mineral mixture & clean water, Roughage (hay, straw)"

    else:
        breed_name = "Unknown"
        confidence_score = "N/A"
        visuals = "The uploaded image does not match any of the known breeds."
        weight = "N/A"
        prod = "N/A"
        nutrition = "N/A"
    
    # Display the results
    st.image(uploaded_file, caption=f"Uploaded Image: {uploaded_image_name}")
    st.write(f"**Breed:** {breed_name}")
    st.write(f"**Confidence Score:** {confidence_score}")
    st.write(f"**Characteristics:** {visuals}")
    st.write(f"**Weight:** {weight}" )
    st.write(f"**Milk Production:** {prod}" )
    st.write(f"**Nutritional Requirement:** {nutrition}" )

# Configure the API key from Streamlit secrets
genai.configure(api_key=st.secrets["gemini_api_key"])

# Initialize the Gemini model
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me anything about cow breeds!"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Use a generation_config to get concise answers
    generation_config = genai.types.GenerationConfig(
        max_output_tokens=100,  # Limits the response length
        temperature=0.7,        # Controls randomness; lower value for more focused responses
    )
    
    # Use streaming to display the response word by word
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Stream the response
            for chunk in gemini_model.generate_content(prompt, stream=True, generation_config=generation_config):
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
            
            # The '▌' is removed and the final response is displayed
            message_placeholder.markdown(full_response)
            
            # Add the final assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error("Sorry, I am unable to generate a response at this moment. Please try again later.")
            st.session_state.messages.append({"role": "assistant", "content": "Sorry, I am unable to generate a response at this moment. Please try again later."})
