from langchain_core.prompts import PromptTemplate

# This prompt assigns a score based on matching result
score_prompt = PromptTemplate(
    input_variables=["match"],
    template="""
You are an AI system that scores a candidate based on resume-job match.

Your task:
- Give a score between 0 to 100

Rules:
- Higher match → higher score
- Lower match → lower score
- Do NOT assume anything
- Return only the score number (no explanation)

Match Result:
{match}
"""
)