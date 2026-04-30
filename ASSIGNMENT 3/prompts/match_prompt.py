from langchain_core.prompts import PromptTemplate

# This prompt compares resume with job description
match_prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template="""
You are an AI system that compares a resume with a job description.

Your task:
- Identify matching skills
- Identify missing skills

Rules:
- Do NOT assume anything
- Only use given data
- Be clear and structured

Resume:
{resume}

Job Description:
{job}
"""
)