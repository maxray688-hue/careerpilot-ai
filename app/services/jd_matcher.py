from app.services.nvidia_client import ask_ai
from app.prompts.jd_prompt import JD_MATCH_PROMPT


def match_resume(resume_text, jd_text):

    prompt = JD_MATCH_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )

    return ask_ai(prompt)