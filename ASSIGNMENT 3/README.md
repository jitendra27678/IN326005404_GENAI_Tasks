# 🤖 AI Resume Screening System with LangChain

## 📌 Project Overview

This project is an AI-powered Resume Screening System that evaluates candidates based on a given job description.

It uses a structured pipeline to:

* Extract skills from resumes
* Match them with job requirements
* Assign a score
* Provide explanation for the score

---

## 🎯 Objective

To build a modular LLM-based system that can:

* Automate resume evaluation
* Provide scoring (0–100)
* Generate explainable results
* Demonstrate LangChain pipeline design

---

## 🧠 Pipeline Flow

Resume → Skill Extraction → Matching → Scoring → Explanation

---

## ⚙️ Features

* 🔍 Skill Extraction from resume
* 🔗 Resume vs Job Matching
* 📊 Scoring system (0–100)
* 🧾 Explainable AI output
* 🧩 Modular design using prompts and chains

---

## 📁 Project Structure

```
ASSIGNMENT 3/
├── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   └── explain_prompt.py
│
├── chains/
│   └── pipeline.py
│
├── data/
│   ├── job.txt
│   ├── strong.txt
│   ├── average.txt
│   └── weak.txt
│
└── main.py
```

---

## 🛠️ Technologies Used

* Python
* LangChain
* HuggingFace Transformers (GPT-2)
* LangSmith (Tracing)

---

## 🔄 How It Works

### Step 1: Skill Extraction

Extracts:

* Skills
* Experience
* Tools

### Step 2: Matching

Compares resume with job description:

* Matching skills
* Missing skills

### Step 3: Scoring

Assigns score between 0–100 based on match quality

### Step 4: Explanation

Provides reasoning for the assigned score

---

## 📊 Example Output

```
===== WEAK CANDIDATE =====

Extracted Info:
Candidate has knowledge of Excel and Word...

Matching Result:
Missing skills: Python, Machine Learning...

Score:
15

Explanation:
Candidate lacks required technical skills...
```

---

## 🔍 LangSmith Tracing

LangSmith tracing was configured to monitor pipeline execution.

Due to the use of a local HuggingFace model, detailed LLM-level tracing is limited, but LangChain pipeline tracing was successfully demonstrated.

---

## 🚀 How to Run

1. Clone repository
2. Navigate to ASSIGNMENT 3 folder
3. Run:

```
python main.py
```

---

## 📌 Key Learnings

* Building modular AI pipelines
* Prompt engineering for structured output
* Designing explainable AI systems
* Understanding LLM limitations
* Debugging using LangSmith

---

## 🎯 Conclusion

This project demonstrates how to build a real-world AI system using LangChain concepts such as prompts, chains, and structured pipelines.

It showcases how LLMs can be used for practical applications like resume screening with explainable outputs.
