from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI system that extracts structured information from resumes.

Extract the following:
- Skills
- Experience
- Tools

Rules:
- Do NOT assume anything
- Only use given data

Resume:
{resume}
"""
)