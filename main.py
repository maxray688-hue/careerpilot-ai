from app.services.resume_reader import read_resume
from app.services.jd_reader import read_jd
from app.services.jd_matcher import match_resume

resume = read_resume("uploads/resume.pdf")
jd = read_jd("uploads/job_description.txt")

result = match_resume(resume, jd)

print("\n========== JD MATCH REPORT ==========\n")
print(result)