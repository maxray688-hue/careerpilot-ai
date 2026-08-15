from app.agents.cover_letter_agent import generate_cover_letter
from app.utils.report_writer import save_report

cover_letter = generate_cover_letter(
    "uploads/resume.pdf",
    "uploads/job_description.txt"
)

report_path = save_report("cover_letter.txt", cover_letter)

print("\n========== COVER LETTER ==========\n")
print(cover_letter)

print(f"\nCover letter saved successfully: {report_path}")