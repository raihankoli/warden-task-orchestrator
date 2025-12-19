from app.schemas import AgentState

def response_node(state: AgentState) -> AgentState:
    intent = state.get("intent", {})
    reasoning = state.get("reasoning", [])
    plan = state.get("plan", [])
    action = state.get("action", {})
    decision_path = state.get("decision_path", [])

    primary = intent.get("primary", {})
    confidence = primary.get("confidence", 0.0)

    response = {
        "summary": f"Detected intent: {primary.get('name', 'unknown')}",
        "confidence": confidence,
        "reasoning": reasoning,
        "recommended_steps": plan,
        "action": action,
        "decision_path": decision_path,
        "next_action": action.get(
            "message",
            "No further action decided"
        )
    }

    return {
        **state,
        "response": response
    }
