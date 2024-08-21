import streamlit as st
import google.generativeai as genai # type: ignore
import os
from dotenv import load_dotenv
from fpdf import FPDF # type: ignore
from io import BytesIO

load_dotenv()
api_key = os.getenv('api_key')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Learning Roadmap Generator")
st.title("Learning Roadmap Generator")
st.subheader("Get a comprehensive roadmap to learn any topic from beginner to advanced")

user_topic = st.text_input("Enter the topic you want to learn:")

if user_topic:
    prompt = f"Create a comprehensive roadmap to learn {user_topic} from beginner to advanced, including blog articles and YouTube videos. Structure the roadmap in clear stages (e.g., Beginner, Intermediate, Advanced) and provide specific resources for each stage and make sure that all the URL of the links are working"
    
    with st.spinner("Generating your learning roadmap..."):
        try:
            response = model.generate_content(prompt)
            roadmap = response.text
            st.subheader(f"Learning Roadmap for {user_topic}")
            st.markdown(roadmap)
           
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, roadmap)
           
            pdf_buffer = BytesIO()
            pdf_string = pdf.output(dest='S').encode('latin-1')
            pdf_buffer.write(pdf_string)
            pdf_buffer.seek(0)
           
            pdf_data = pdf_buffer.getvalue()
           
            st.download_button(
                label="Download Roadmap as PDF",
                data=pdf_data,
                file_name=f"{user_topic}_roadmap.pdf",
                mime="application/pdf"
            )
           
        except Exception as e:
            st.error(f"An error occurred while generating the roadmap. Please try again. Error details: {str(e)}")
