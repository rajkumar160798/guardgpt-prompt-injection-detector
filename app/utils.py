import re

# Define risky prompt patterns
regex_patterns = [
    r"ignore previous instructions",
    r"act as .*",
    r"pretend to be",
    r"you are not .*chatgpt",
    r"bypass .*safety.*",
    r"respond without restrictions",
    r"simulate .*scenario",
    r"disregard content policy",
    r"hacking tips",
    r"make a bomb",
    r"illegal goods",
    r"fake passport",
    r"deep web",
    r"credit card fraud",
    r"phishing email",
    r"racist joke",
    r"sexist joke",
    r"violent joke",
    r"self-harm",
    r"suicide",
    r"child exploitation",
    r"drug manufacturing",
    r"weapon manufacturing",
    r"human trafficking",
    r"money laundering",
    r"terrorism",
    r"assassination",
    r"extreme violence",
    r"hate speech",
    r"bullying",
    r"harassment",
    r"stalking"
]


def regex_score(prompt: str) -> int:
    matches = [p for p in regex_patterns if re.search(p, prompt, re.IGNORECASE)]
    return len(matches), matches
    # return len(matches), matches
def check_prompt(prompt: str) -> dict:
    """
    Check the prompt for risky patterns and return a risk score.
    """
    matches = [p for p in regex_patterns if re.search(p, prompt, re.IGNORECASE)]
    return {"score": len(matches), "matches": matches}