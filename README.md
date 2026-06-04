# 🌟 Padhai Dost

An AI-powered study companion for Indian students that explains NCERT topics in simple Hinglish, generates revision notes, and creates practice questions from topics or uploaded PDFs.

---

## 🎯 Why I Built This?

Many Indian students understand concepts better in a mix of Hindi and English rather than textbook English alone.

I built Padhai Dost to act like a study buddy that explains NCERT topics in simple Hinglish, generates revision notes, and creates practice questions from chapters and PDFs.

The inspiration came from my younger brother (Class 6) and sister (Class 9), who often struggled with English-heavy textbook explanations.

---

## ✨ Features

### 🤖 AI Topic Explainer
- Select Class (6–10)
- Select Subject (Science, Maths, SST)
- Ask questions in natural language
- Get easy-to-understand Hinglish explanations

### 📝 Revision Notes Generator
- Generate notes from a topic
- Generate notes directly from uploaded chapter PDFs
- English Notes section
- Hinglish Explanation section
- Important Exam Points
- Quick Revision Summary

### 📄 PDF Learning
- Upload digital NCERT PDFs
- Extract chapter content using PyPDF2
- Use chapter content as context for note generation
- Supports chapter-based learning

### ❓ Practice Question Generator
Generate NCERT-style questions from:
- Topic input
- Uploaded PDFs

Question Modes:
- Mixed
- MCQ Only
- Fill in the Blanks
- Short Answer
- Exam Prep Mode

Includes:
- Answers
- Explanations
- Student-friendly format

### 🎓 NCERT Focused
Designed specifically for:
- Class 6
- Class 7
- Class 8
- Class 9
- Class 10

Subjects:
- Science
- Maths
- SST

---

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenRouter API
- PyPDF2
- Git
- GitHub

---

## 📚 What I Learned

Building Padhai Dost helped me learn:

- Prompt Engineering
- Building applications with LLM APIs
- Streamlit web app development
- Environment variable management using `.env`
- Git and GitHub workflows
- PDF text extraction using PyPDF2
- Context-based AI responses
- Basic Retrieval-Augmented Generation (RAG) concepts
- Product building and user testing

---

## 🚀 How It Works

### Topic Explainer

Student enters:

```text
What is Photosynthesis?
```

Output:

```text
Photosynthesis matlab plants apna khana khud banate hain
using sunlight, water aur carbon dioxide.
```

### PDF Notes

1. Upload chapter PDF
2. Extract chapter content
3. Generate revision notes automatically

### Practice Questions

1. Select question mode
2. Enter topic or upload PDF
3. Generate NCERT-style practice questions

---

## 📂 Project Structure

```text
padhai-dost/
│
├── app.py
├── README.md
├── .gitignore
├── .env
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/mantashaamin/padhai-dost.git
cd padhai-dost
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 🌟 Future Improvements

- Streamlit Cloud Deployment
- Better Notes Formatting
- Chapter-wise MCQ Bank
- Quiz Mode
- Student Progress Tracking
- OCR Support for Scanned PDFs
- Multi-language Support

---

## 👩‍💻 Built By

**Mantasha Parween**

B.Tech Student | Builder | AI Enthusiast

GitHub: https://github.com/mantashaamin

Hashnode: https://padhai-dost.hashnode.dev

---

## ❤️ Padhai Dost

Making NCERT learning simpler, friendlier, and more accessible for Indian students through AI.
