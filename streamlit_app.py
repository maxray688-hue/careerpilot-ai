from concurrent.futures import ThreadPoolExecutor
import time

import streamlit as st

from app.agents.cover_letter_agent import generate_cover_letter_from_text
from app.agents.resume_analyzer import analyze_resume_from_text
from app.services.jd_reader import read_jd
from app.services.resume_reader import read_resume


st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

st.title("🚀 CareerPilot AI")
st.caption("AI Powered Resume Analyzer & Cover Letter Generator")
st.divider()

uploaded_resume = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("📋 Paste Job Description", height=250)


def run_analysis(resume_text: str, jd_text: str) -> tuple[str, str]:
    """Run independent LLM requests concurrently after inputs are read once."""
    with ThreadPoolExecutor(max_workers=2) as executor:
        resume_future = executor.submit(analyze_resume_from_text, resume_text)
        cover_letter_future = executor.submit(
            generate_cover_letter_from_text, resume_text, jd_text
        )
        return resume_future.result(), cover_letter_future.result()


if st.button("🚀 Analyze Resume", use_container_width=True):
    if uploaded_resume is None:
        st.error("Please upload a Resume.")
    elif not job_description.strip():
        st.error("Please paste a Job Description.")
    else:
        start = time.perf_counter()
        progress_bar = st.progress(0)
        status = st.empty()

        try:
            status.write("📄 Reading resume and job description...")
            progress_bar.progress(15)

            # The PDF and JD are parsed exactly once for this run.  Keeping the
            # content in memory also avoids shared uploads/resume.pdf files.
            resume_text = read_resume(uploaded_resume.getvalue())
            jd_text = read_jd(job_description)

            if not resume_text.strip():
                raise ValueError("No readable text was found in the uploaded PDF.")

            status.write("🤖 Analyzing resume and generating cover letter...")
            progress_bar.progress(45)

            with st.spinner("AI is working on both results..."):
                resume_report, cover_letter = run_analysis(resume_text, jd_text)

            progress_bar.progress(100)
            status.write("✅ Analysis completed")
            st.caption(f"Completed in {time.perf_counter() - start:.1f} seconds")
            st.success("🎉 Analysis Completed Successfully!")

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("📊 Resume Analysis")
                st.write(resume_report)
                st.download_button(
                    "⬇ Download Resume Analysis",
                    resume_report,
                    file_name="resume_analysis.txt",
                    mime="text/plain",
                )

            with col2:
                st.subheader("✉️ Cover Letter")
                st.write(cover_letter)
                st.download_button(
                    "⬇ Download Cover Letter",
                    cover_letter,
                    file_name="cover_letter.txt",
                    mime="text/plain",
                )
        except Exception as error:
            progress_bar.empty()
            status.empty()
            st.error(f"Unable to complete the analysis: {error}")
