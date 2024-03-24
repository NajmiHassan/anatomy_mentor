import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("api_key")

# Set up Google Gemini-Pro AI model
genai.configure(api_key=GOOGLE_API_KEY) 
config = {
    "temperature": 0.8,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-pro", generation_config=config)

def analyze_anatomy_topic(topic):
    """
    This function analyzes the user-entered anatomy topic and returns a formatted string
    containing relevant information.
    """
    # Generate content using the Gemini AI model
    prompt = f"Explain anatomy for this topic: {topic}"
    response = model.generate_content(prompt)
    return response.text if response else f"No analysis available for {topic}."

def analyze_anatomy_questions(topic, questions):
    """
    This function analyzes the user-entered anatomy topic and returns a formatted string
    containing relevant information.
    """
    # Generate content using the Gemini AI model
    prompt = f"generate {questions} mcqs questions for this topic: {topic}"
    response = model.generate_content(prompt)
    return response.text if response else f"No analysis available for {topic}."

def anatomy_picture_request(image):
    """
    This function handles the request for analyzing an anatomical structure image.
    """
    # Open the uploaded image file
    img = Image.open(image)
    
    # Display the uploaded image
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    
    # Analyze the image using the Gemini AI model
    prompt = f"Explain the anatomy of the structure in this image."
    response = model.generate_content(prompt)
    
    return response.text if response else f"No analysis available for the uploaded image." 

def stream_data(data):
    for word in data.split(" "):
        yield word + " "
        time.sleep(0.05) 


def main():
    st.set_page_config(page_title="AnatomyMentor", layout="wide")

    st.image("images/image.png")
    st.markdown("*AnatomyMentor* Our anatomy tutoring app is designed to assist medical students in learning complex anatomical concepts with ease. Through interactive lessons, visual aids, and personalized learning features, students can delve into various anatomy topics, such as nerves, muscles, and organs. The app also offers question generation for practice and incorporates image processing capabilities to analyze uploaded anatomical structure images. By leveraging the power of AI, our app aims to provide comprehensive and tailored support to enhance the anatomy learning experience for students.")

    # Sidebar
    with st.sidebar:
        st.header("Controls")
        anatomy_topic = st.text_area("Enter the anatomy topic or specific area you would like to learn more about:", height=10)
        anatomy_mcqs = st.text_input("How many multiple-choice questions would you like to generate for practicing anatomy concepts?", value='10')
        anatomy_pic = st.file_uploader("Upload an image of the anatomical structure you would like to learn more about:")

        generate_plan_btn = st.button("Generate analysis and questions")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Anatomy Topic Analysis:")
        if anatomy_topic:  # Check if user entered a topic
            analysis_output = analyze_anatomy_topic(anatomy_topic)
            st.write_stream(stream_data(analysis_output))
        else:
            st.write("Please enter an anatomy topic in the sidebar.")

        st.divider()

    with col2:
        st.subheader("Question Generation:")
        if generate_plan_btn:  # Check if generate button is clicked
            question_output = analyze_anatomy_questions(anatomy_topic, anatomy_mcqs)
            st.write_stream(stream_data(question_output))  # Placeholder action

        st.divider()

        st.subheader("Anatomical Structure Image Analysis and Description:")
        if anatomy_pic is not None:
           output =  anatomy_picture_request(anatomy_pic)
           st.write_stream(stream_data(output))
        else:
            st.write("Please upload an image for analysis.")

if __name__ == "__main__":
    main()
