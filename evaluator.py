import json
from datetime import datetime

def classify_prompt(prompt):
    jailbreak_keywords = [
        "ignore instructions",
        "bypass",
        "developer mode",
        "forget rules",
        "reveal system prompt",
        "hidden instructions"
    ]

    for keyword in jailbreak_keywords:
        if keyword.lower() in prompt.lower():
            return "jailbreak_attempt"

    return "safe"


def score_prompt(prompt):
    label = classify_prompt(prompt)

    if label == "jailbreak_attempt":
        risk_score = 0.9
    else:
        risk_score = 0.1

    return {
        "prompt": prompt,
        "label": label,
        "risk_score": risk_score,
        "timestamp": str(datetime.now())
    }


def save_results(results, filename="results.json"):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
