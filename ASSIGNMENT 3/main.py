import os

# =========================
# LangSmith Setup
# =========================
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_PROJECT"] = "resume-screening-project"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"


# =========================
# LangSmith Trace Trigger (IMPORTANT)
# =========================
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

trace_prompt = PromptTemplate(
    input_variables=["text"],
    template="Start Resume Screening: {text}"
)

trace_chain = trace_prompt | RunnableLambda(lambda x: x)

# THIS LINE TRIGGERS TRACE
trace_chain.invoke({"text": "Pipeline Started"})


# =========================
# Import Prompts
# =========================
from prompts.extract_prompt import extract_prompt
from prompts.match_prompt import match_prompt
from prompts.score_prompt import score_prompt
from prompts.explain_prompt import explain_prompt


# =========================
# Import Pipeline
# =========================
from chains.pipeline import process_resume


# =========================
# Load Data
# =========================
job = open("data/job.txt").read()
strong = open("data/strong.txt").read()
average = open("data/average.txt").read()
weak = open("data/weak.txt").read()


# =========================
# Combine Prompts
# =========================
prompts = {
    "extract": extract_prompt,
    "match": match_prompt,
    "score": score_prompt,
    "explain": explain_prompt
}


# =========================
# Output Formatter
# =========================
def print_result(title, result):
    print(f"\n===== {title} =====")
    
    print("\n🔹 Extracted Info:")
    print(result["extract"])
    
    print("\n🔹 Matching Result:")
    print(result["match"])
    
    print("\n🔹 Score:")
    print(result["score"])
    
    print("\n🔹 Explanation:")
    print(result["explain"])


# =========================
# Run Pipeline
# =========================

# Strong
strong_result = process_resume(strong, job, prompts)
print_result("STRONG CANDIDATE", strong_result)

# Average
average_result = process_resume(average, job, prompts)
print_result("AVERAGE CANDIDATE", average_result)

# Weak
weak_result = process_resume(weak, job, prompts)
print_result("WEAK CANDIDATE", weak_result)