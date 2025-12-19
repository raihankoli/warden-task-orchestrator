from typing import List
from app.schemas import IntentResult, MultiIntentResult

def detect_intent(query: str) -> MultiIntentResult:
    query_lower = query.lower()

    INTENT_RULES = {
    "bridge_funds": {
        "keywords": ["bridge", "transfer", "move"],
        "weight": 1.0
    },
    "risk_check": {
        "keywords": ["safe", "risk", "secure", "audit"],
        "weight": 0.7
    },
    "general_query": {
        "keywords": [],
        "weight": 0.3
    }
    }

    def score_intent(query: str, rule: dict) -> float:
    score = 0.0
    for kw in rule["keywords"]:
        if kw in query:
            score += 1.0
    return score * rule["weight"]


def detect_intent(query: str) -> MultiIntentResult:
    query_lower = query.lower()
    scored = []

    for name, rule in INTENT_RULES.items():
        score = score_intent(query_lower, rule)
        if score > 0:
            scored.append({
                "name": name,
                "score": score
            })

    if not scored:
        return {
            "primary": {
                "name": "general_query",
                "confidence": 0.4,
                "reason": "No strong intent detected"
            },
            "secondary": []
        }

    scored.sort(key=lambda x: x["score"], reverse=True)

    primary = scored[0]
    secondary = scored[1:]

    confidence = min(1.0, primary["score"] / 3)

    return {
        "primary": {
            "name": primary["name"],
            "confidence": round(confidence, 2),
            "reason": "Highest weighted intent score"
        },
        "secondary": [
            {
                "name": s["name"],
                "confidence": round(min(1.0, s["score"] / 3), 2),
                "reason": "Supporting signal detected"
            }
            for s in secondary
        ]
    }
    
    if not intents:
        intents.append({
            "name": "general_query",
            "confidence": 0.6,
            "reason": "No clear action keyword detected"
        })

    return {
    "primary": intents[0],
    "secondary": intents[1:] if len(intents) > 1 else []
    }
