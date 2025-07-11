import streamlit as st
import openai
import fitz  # PyMuPDF

from prompts import build_prompt
from resume_parser import extract_text_from_pdf

openai.api_key = st.secrets["OPENAI_API_KEY"]  # ✅ FIXED

st.set_page_config(page_title="Smart Cover Letter Generator", layout="centered")
st.title("📄 Smart Cover Letter Generator")

st.write("✅ App started")  # Debug marker

with st.sidebar:
    st.header("Settings")
    tone = st.selectbox("Select Tone", ["Formal", "Enthusiastic", "Persuasive", "Confident"])
    generate_button = st.button("Generate Cover Letter")

st.markdown("---")

resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
if resume_file:
    st.write("✅ Resume uploaded")  # Debug marker

job_description = st.text_area("Paste Job Description")
if job_description:
    st.write("✅ Job description pasted")  # Debug marker

if generate_button:
    if not resume_file or not job_description:
        st.warning("Please upload your resume and paste a job description.")
    else:
        with st.spinner("Reading resume and preparing prompt..."):
            resume_text = extract_text_from_pdf(resume_file)
            prompt = build_prompt(resume_text, job_description, tone)

        try:
            with st.spinner("Generating cover letter using GPT-4..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that writes professional cover letters."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                letter = response.choices[0].message.content
                st.success("Cover letter generated!")
                st.text_area("Your Cover Letter", value=letter, height=400)
                st.download_button("Download as .txt", letter, file_name="cover_letter.txt")
        except Exception as e:
            st.error(f"Error generating letter: {e}")
