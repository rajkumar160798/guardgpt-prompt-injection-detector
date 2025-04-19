from fastapi import FastAPI
from app.schema import PromptRequest, PromptResponse
from app.model import predict_prompt
from app.utils import regex_score

app = FastAPI()

@app.post("/analyze-prompt", response_model=PromptResponse)
def analyze_prompt(req: PromptRequest):
    prompt = req.prompt
    prob = predict_prompt(prompt)
    regex_hits, patterns = regex_score(prompt)

    # Hybrid scoring logic
    score = (prob * 60) + (regex_hits * 20) # Normalize: ML=70%, Regex=30%
    score = min(score, 100)

    # Flag generation
    flags = []
    if prob > 0.7:
        flags.append("high_model_score")
    if regex_hits > 0:
        flags.append("regex_match")

    verdict = "High Risk" if score >= 55 else "Moderate" if score > 35 else "Low Risk"
    if score > 80:
        verdict = "Critical Risk"
    elif score > 60:
        verdict = "High Risk"
    elif score > 40:
        verdict = "Moderate Risk"
    elif score > 20:
        verdict = "Low Risk"
    else:
        verdict = "Safe"
    # Add regex patterns to flags
    if patterns:
        flags.extend(patterns)
    # Add regex patterns to flags
    if patterns:
        flags.extend(patterns)
    # Return the response
    return PromptResponse(
        risk_score=round(score, 2),
        flags=flags + patterns,
        verdict=verdict
    )

