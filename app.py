from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import PyPDF2
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

st.title("📚 Padhai Dost")
st.subheader("Aapka AI Study Companion!")

subject = st.selectbox("Subject chuno:", ["Science", "Maths", "SST"])
grade = st.selectbox("Class chuno:", ["Class 6", "Class 7", "Class 8", "Class 9", "Class 10"])
question = st.text_input("Apna sawaal likho:")

if st.button("Samjhao! 🚀"):
    if question:
        with st.spinner("Padhai Dost soch raha hai..."):
            response = client.chat.completions.create(
                model="openrouter/auto",
                messages=[{
                    "role": "user",
                    "content": f"You are Padhai Dost, a friendly study companion for Indian students. Explain in simple Hinglish (mix of Hindi and English). Student is in {grade}, subject is {subject}. Question: {question}"
                }]
            )
            st.write(response.choices[0].message.content)
    else:
        st.warning("Pehle sawaal likho!")
# ADD NEW CODE HERE  FOR NOTES 👇
st.divider()

st.subheader("📄 PDF se Padho!")

uploaded_file = st.file_uploader("Chapter ka PDF upload karo:", type="pdf")
pdf_text = ""
if uploaded_file:
    # Read PDF text
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        pdf_text += page.extract_text()
    st.success("PDF pad liya! Ab notes ya questions maango 😊")
topic = st.text_input("Topic likho (notes ke liye):")
if st.button("Notes banao! 📝"):
    if topic or uploaded_file:
        with st.spinner("Notes ban rahe hain..."):
            # Decide content based on PDF or topic
            if uploaded_file:
                content = f"You are Padhai Dost. Create clean revision notes in english also immediately their hinglish version below it for {grade} student. Subject: {subject}. Here is the chapter content: {pdf_text}. Create detailed notes from this content. NO Hindi script."
            else:
                content = f"You are Padhai Dost. Create clean revision notes in Hinglish for {grade} student. Subject: {subject}. Topic: {topic}. STRICTLY Hinglish only, NO Hindi script."
            response = client.chat.completions.create(
                model="openrouter/auto",
                messages=[{
                    "role": "user",
                    "content": content
                }]
            )
            st.write(response.choices[0].message.content)
    else:
        st.warning("PDF upload karo ya Pehle topic likho!")
# ADD NEW CODE HERE  FOR PRACTICE QUESTION 👇
st.divider()
topic = st.text_input("Topic Likho(Practice question ke liye ):")
if st.button("practice question"):
    if topic :
        with st.spinner("Practice Question bana raha hai"):
            response = client.chat.completions.create(
                model = "openrouter/auto",
                messages=[{
                    "role" : "user",
                   "content": f"You are Padhai Dost. Generate 5 NCERT-style practice questions for {grade} student. Subject: {subject}. Topic: {topic}. Format: Question in English with Hinglish translation in brackets. Answer in proper NCERT English terms with Hinglish explanation in brackets. Include MCQ, fill in the blanks and short answer types. STRICTLY use Hinglish only - NO Hindi script/Devanagari script allowed anywhere. Write everything in Roman letters only. Example heading: '1. MCQ (Multiple Choice Question)' NOT '1. MCQ (बहुविकल्पीय प्रश्न)'"
                }]
            )
            st.write(response.choices[0].message.content)
    else :
        st.warning("pehle topic likho!")