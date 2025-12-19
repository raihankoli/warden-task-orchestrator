from typing import List
from app.schemas import IntentResult, MultiIntentResult

def detect_intent(query: str) -> MultiIntentResult:
    query_lower = query.lower()

    intents: List[IntentResult] = []

    # Primary intent detection
    if "bridge" in query_lower or "transfer" in query_lower:
        intents.append({
            "name": "bridge_funds",
            "confidence": 0.9,
            "reason": "User wants to move assets across chains"
        })

    if "safe" in query_lower or "risk" in query_lower:
        intents.append({
            "name": "risk_check",
            "confidence": 0.7,
            "reason": "User expresses concern about safety or risk"
        })

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
