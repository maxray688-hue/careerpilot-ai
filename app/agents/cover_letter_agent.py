from app.services.resume_reader import read_resume
from app.services.jd_reader import read_jd
from app.services.nvidia_client import ask_ai
from app.prompts.cover_letter_prompt import get_cover_letter_prompt


def generate_cover_letter(resume_path, jd_path):
    resume_text = read_resume(resume_path)
    jd_text = read_jd(jd_path)

    prompt = get_cover_letter_prompt(resume_text, jd_text)

    cover_letter = ask_ai(prompt)

    return cover_letter