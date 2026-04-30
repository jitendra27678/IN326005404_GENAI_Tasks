from transformers import pipeline
import re

# load free model
generator = pipeline("text-generation", model="gpt2")


# function to call model and clean output
def run_llm(text):
    result = generator(text, max_new_tokens=100)[0]["generated_text"]

    # remove original prompt from output
    clean_output = result.replace(text, "").strip()

    return clean_output


# main pipeline function
def process_resume(resume, job, prompts):

    # Step 1: Extract
    extract_output = run_llm(
        prompts["extract"].format(resume=resume)
    )

    # Step 2: Match
    match_output = run_llm(
        prompts["match"].format(resume=resume, job=job)
    )

    # Step 3: Score
    raw_score = run_llm(
        prompts["score"].format(match=match_output)
    )

    # clean score (extract only number)
    score_numbers = re.findall(r'\d+', raw_score)
    score_output = score_numbers[0] if score_numbers else "0"

    # Step 4: Explain
    explain_output = run_llm(
        prompts["explain"].format(resume=resume, score=score_output)
    )

    return {
        "extract": extract_output,
        "match": match_output,
        "score": score_output,
        "explain": explain_output
    }