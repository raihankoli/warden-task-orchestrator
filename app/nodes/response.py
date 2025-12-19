from app.schemas import AgentState

CONFIDENCE_THRESHOLD = 0.75


def response_node(state: AgentState) -> AgentState:
    intent = state.get("intent", {})
    reasoning = state.get("reasoning", [])
    plan = state.get("plan", [])

    primary = intent.get("primary", {})
    confidence = primary.get("confidence", 0.0)
    intent_name = primary.get("name", "unknown")

    response = {
        "summary": f"Detected intent: {intent_name}",
        "confidence": confidence,
        "reasoning": reasoning,
        "recommended_steps": plan,
        "next_action": (
            "Proceed carefully following the steps above"
            if confidence >= CONFIDENCE_THRESHOLD
            else "Please clarify your goal for better guidance"
        ),
    }

    return {
        **state,
        "response": response,
    }
