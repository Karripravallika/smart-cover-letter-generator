def build_prompt(resume_text: str, job_description: str, tone: str) -> str:
    return f"""
You are an expert in writing cover letters.

Write a {tone.lower()} cover letter tailored for the job described below. Use the resume content to highlight the candidate's strengths. Format the letter properly.

RESUME:
\"\"\"
{resume_text}
\"\"\"

JOB DESCRIPTION:
\"\"\"
{job_description}
\"\"\"

The cover letter should be 3–4 paragraphs, concise, and compelling.
"""
