from langchain_core.prompts import PromptTemplate

# This prompt explains the score
explain_prompt = PromptTemplate(
    input_variables=["resume", "score"],
    template="""
You are an AI system that explains candidate evaluation.

Your task:
- Explain why this score was given

Rules:
- Base explanation only on resume data
- Do NOT assume anything
- Be clear and concise

Resume:
{resume}

Score:
{score}
"""
)