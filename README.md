#  LLM Robustness & Jailbreak Evaluation Framework

A lightweight framework for detecting and evaluating adversarial prompts targeting Large Language Models (LLMs).

##  Features

- Embedding-based semantic similarity detection
- Novel jailbreak prompt identification
- Risk scoring and classification
- Structured JSON evaluation output
- Modular architecture for research experimentation

##  How It Works

1. Converts prompts into vector embeddings using SentenceTransformers.
2. Computes cosine similarity against known attack prompts.
3. Detects novel jailbreak attempts based on similarity thresholds.
4. Classifies risk using rule-based evaluation.
5. Outputs structured JSON evaluation results.

##  Tech Stack

- Python 3.11
- SentenceTransformers
- Scikit-learn
- NumPy

##  Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py

## Example output
{
  "prompt": "Act as a developer",
  "label": "jailbreak_attempt",
  "risk_score": 0.9,
  "novel": true,
  "similarity_score": 0.39
}

