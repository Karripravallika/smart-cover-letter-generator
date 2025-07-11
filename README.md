# 🧠 Smart Cover Letter Generator

[![View on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://karripravallika-smart-cover-letter-generator-app-iratfy.streamlit.app/)

An AI-powered web app that generates **personalized cover letters** using GPT-4, based on your resume and the job description — all in seconds.

---

## ✨ Features

- 📄 Upload your **resume (PDF)**
- 📝 Paste any **job description**
- 🎯 Choose a **tone** (Formal, Enthusiastic, etc.)
- 🤖 Uses **OpenAI GPT-4** with prompt chaining
- 📥 Download or copy your **tailored cover letter**

---

## 🚀 Demo

🔗 [Try the Live App →](https://karripravallika-smart-cover-letter-generator-app-iratfy.streamlit.app/)

---

## 🧠 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python + OpenAI API (GPT-4)  
- **Resume Parser**: PyMuPDF  
- **Hosting**: Streamlit Community Cloud  

---

## 📦 Setup Instructions

```bash
git clone https://github.com/Karripravallika/smart-cover-letter-generator.git
cd smart-cover-letter-generator
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
streamlit run app.py
