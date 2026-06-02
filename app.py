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
                content = f"""
                You are Padhai Dost.
Student Class: {grade}
Subject: {subject}

Chapter Content:
{pdf_text}

Create EXAM-ORIENTED REVISION NOTES from this chapter.

For every topic include:

## English Notes
- Key concepts
- Definitions
- Important facts

## Hinglish Samjho
- Explain like a friendly teacher
- English alphabets only
- No Hindi script

## Important Exam Points

## Quick Revision

After all topics add:

# Chapter Summary

# 5 Second Revision

RULES:
- Use headings and bullet points
- Use tables when useful
- Do not simply translate English into Hinglish
- Focus on understanding and exam preparation
- Suitable for Class {grade}
"""
            else:
                content = f"""
You are Padhai Dost.
Create EXAM-ORIENTED REVISION NOTES for a Class {grade} student.

Subject: {subject}
Topic: {topic}

OUTPUT FORMAT:

# Topic Name

## English Notes

## Hinglish Samjho

## Important Exam Points

## Quick Revision

## 5 Second Revision

RULES:
- Use simple language
- Explain concepts clearly
- Hinglish must use English alphabets only
- No Hindi script
- Use bullet points and tables where useful
- Focus on exam preparation
"""
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
        


   
# ==========================================

# PRACTICE QUESTIONS SECTION

# ==========================================

st.divider()

# Select question type

question_type = st.selectbox(
"Question Type",
[
"Mixed",
"MCQ Only",
"Fill in the Blanks",
"Short Answer",
"Exam Prep Mode"
]
)

# Topic input (used when no PDF is uploaded)

topic = st.text_input("Topic Likho (Practice question ke liye):")

# Generate Questions Button

if st.button("Practice Question"):
    if topic or uploaded_file: # User must either upload a PDF or enter a topic
        with st.spinner("Practice Question bana raha hai..."): 
        # ------------------------------------------
        # PDF MODE
        # Generate questions from uploaded chapter
        # ------------------------------------------
            if uploaded_file:
                content = f"""


Generate 10 NCERT-style practice questions from this chapter.

Class: {grade}
Subject: {subject}

Chapter Content:
{pdf_text}

Include:

* MCQs
* Fill in the blanks
* Short answer questions

Give answers and Hinglish explanations.

Use only Roman letters.
No Hindi script.
"""


        # ------------------------------------------
        # TOPIC MODE
        # Generate questions from entered topic
        # ------------------------------------------
            else:
                content = f"""


Generate 10 NCERT-style practice questions.

Class: {grade}
Subject: {subject}
Topic: {topic}

Include:

* MCQs
* Fill in the blanks
* Short answer questions

Give answers and Hinglish explanations.

Use only Roman letters.
No Hindi script.
"""


        # Send prompt to OpenRouter
        response = client.chat.completions.create(
            model="openrouter/auto",
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ]
        )

        # Display generated questions
        st.write(response.choices[0].message.content)

# User entered nothing
else:
    st.warning("Pehle topic likho ya PDF upload karo!")

