from app.services.resume_reader import read_resume
from app.services.nvidia_client import ask_ai

# Resume read karo
resume_text = read_resume("uploads/resume.pdf")

# AI prompt
prompt = f"""
Analyze this resume.

Resume:
{resume_text}

Give:
1. Professional Summary
2. Strengths
3. Weaknesses
4. ATS Score out of 100
5. Suggested Improvements
"""

response = ask_ai(prompt)

print("\n===== CAREERPILOT AI =====\n")
print(response)