from typing import List
from app.schemas import MultiIntentResult

def build_plan(intents: MultiIntentResult) -> List[str]:
    steps: List[str] = []

    primary = intents["primary"]["name"]
    secondary = intents.get("secondary") or []

    if primary == "bridge_funds":
        steps.extend([
            "Select a trusted bridge protocol",
            "Verify source and destination chains",
            "Confirm token support and fees"
        ])

    elif primary == "general_query":
        steps.append(
            "Clarify user goal before taking action"
        )

    for intent in secondary:
        if intent["name"] == "risk_check":
            steps.extend([
                "Review bridge security audits",
                "Check recent incidents or exploits",
                "Consider using a small test transaction first"
            ])

    return steps
