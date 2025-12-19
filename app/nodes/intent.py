from typing import List
from app.schemas import IntentResult, MultiIntentResult

# Global intent rules with weights
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
    """
    Calculate weighted score for an intent rule
    """
    score = 0.0
    for kw in rule["keywords"]:
        if kw in query:
            score += 1.0
    return score * rule["weight"]


def detect_intent(query: str) -> MultiIntentResult:
    """
    Detect primary and secondary intents using weighted scoring
    """
    query_lower = query.lower()
    scored: List[dict] = []

    for name, rule in INTENT_RULES.items():
        score = score_intent(query_lower, rule)
        if score > 0:
            scored.append({
                "name": name,
                "score": score
            })

    # Fallback: no intent detected
    if not scored:
        return {
            "primary": {
                "name": "general_query",
                "confidence": 0.4,
                "reason": "No strong intent detected"
            },
            "secondary": []
        }

    # Sort by score (highest first)
    scored.sort(key=lambda x: x["score"], reverse=True)

    primary = scored[0]
    secondary = scored[1:]

    primary_confidence = min(1.0, primary["score"] / 3)

    return {
        "primary": {
            "name": primary["name"],
            "confidence": round(primary_confidence, 2),
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

def resolve_intent_conflicts(intent_result: MultiIntentResult) -> MultiIntentResult:
    """
    Normalize and sanitize intent output for downstream nodes
    """
    primary = intent_result.get("primary", {})
    secondary = intent_result.get("secondary", [])

    # Ensure secondary is always a list
    if secondary is None:
        secondary = []

    # Cap confidence safely
    primary["confidence"] = min(1.0, max(0.0, primary.get("confidence", 0.0)))

    for sec in secondary:
        sec["confidence"] = min(1.0, max(0.0, sec.get("confidence", 0.0)))

    return {
        "primary": primary,
        "secondary": secondary
}
