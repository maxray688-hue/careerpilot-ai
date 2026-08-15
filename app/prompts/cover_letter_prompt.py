def get_cover_letter_prompt(resume_text, job_description):
    return f"""
You are an expert HR recruiter and career coach.

Using the resume and job description below, write a professional cover letter.

Requirements:
- Keep it within 350-450 words.
- Address the hiring manager professionally.
- Highlight relevant experience and achievements.
- Match the candidate's skills with the job description.
- Maintain a confident and professional tone.
- End with a strong closing paragraph.

Resume:
{resume_text}

Job Description:
{job_description}
"""