JD_MATCH_PROMPT = """
You are an expert ATS Resume Analyzer.

Compare the following resume with the given Job Description.

Return:

1. Match Score (0-100)

2. Matching Skills

3. Missing Skills

4. Experience Gap

5. ATS Suggestions

6. Final Recommendation

Resume:

{resume}

Job Description:

{jd}
"""