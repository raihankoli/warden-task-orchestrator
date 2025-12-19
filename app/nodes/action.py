from app.schemas import AgentState

def action_router_node(state: AgentState) -> AgentState:
    """
    Decide what action to take based on plan + intent
    This node MUST be safe and never execute real transactions
    """

    intent = state.get("intent") or {}
    plan = state.get("plan") or []
    decision_path = state.get("decision_path", [])

    primary = intent.get("primary", {})
    intent_name = primary.get("name", "unknown")
    confidence = primary.get("confidence", 0.0)

    # Default safe action
    action = {
        "type": "noop",
        "message": "No executable action selected"
    }

    # High-confidence + plan exists → handoff
    if confidence >= 0.75 and plan:
        if intent_name == "bridge_funds":
            action = {
                "type": "handoff",
                "target": "bridge_agent",
                "message": "Ready to hand off to Bridge Agent"
            }

        elif intent_name == "risk_check":
            action = {
                "type": "analysis",
                "message": "Performing risk analysis before execution"
            }

    # Low confidence → clarification
    if confidence < 0.75:
        action = {
            "type": "clarify",
            "message": "Waiting for user clarification before action"
        }

    return {
        **state,
        "action": action,
        "decision_path": decision_path + ["action"]
            }
