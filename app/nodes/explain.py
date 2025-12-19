from app.schemas import AgentState

def explain_node(state: AgentState) -> AgentState:
    intent = state.get("intent", {})
    primary = intent.get("primary", {})

    explain = {
        "intent": primary.get("name", "unknown"),
        "confidence": primary.get("confidence", 0.0),
        "clarification_needed": primary.get("confidence", 0.0) < 0.75,
        "decision_path": [
            "intent",
            "plan" if state.get("plan") else "clarify",
            "action",
            "response"
        ]
    }

    return {
        **state,
        "explain": explain
    }
