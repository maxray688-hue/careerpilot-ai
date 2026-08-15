from app.services.resume_reader import read_resume
from app.services.nvidia_client import ask_ai


def analyze_resume(resume_path):

    resume_text = read_resume(resume_path)

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume.

Provide:

1. Professional Summary

2. Strengths

3. Weaknesses

4. ATS Score (0-100)

5. Suggestions to improve the resume

Resume:

{resume_text}
"""

    response = ask_ai(prompt)

    return response