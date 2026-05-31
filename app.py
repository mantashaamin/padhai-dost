from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
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
topic = st.text_input("Topic likho (notes ke liye):")
if st.button("Notes banao! 📝"):
    if topic:
        with st.spinner("Notes ban rahe hain..."):
            response = client.chat.completions.create(
                model="openrouter/auto",
                messages=[{
                    "role": "user",
                    "content": f"You are Padhai Dost. Create clean revision notes in Hinglish for {grade} student. Subject: {subject}. Topic: {topic}. IMPORTANT: Use Hinglish only (mix of Hindi and English words), NOT pure Hindi script. Example: 'Plants sunlight use karke apna khana banate hain' not pure Hindi."
                }]
            )
            st.write(response.choices[0].message.content)
    else:
        st.warning("Pehle topic likho!")
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