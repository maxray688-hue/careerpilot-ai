from app.agents.resume_analyzer import analyze_resume
from app.utils.report_writer import save_report

result = analyze_resume("uploads/resume.pdf")

report_path = save_report("resume_analysis.txt", result)

print(f"\nReport saved successfully: {report_path}\n")

print("\n========== RESUME ANALYSIS ==========\n")
print(result)