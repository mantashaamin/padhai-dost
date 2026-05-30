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