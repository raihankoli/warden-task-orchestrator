from app.schemas import AgentState

def action_router_node(state: AgentState) -> AgentState:
    intent = state.get("intent", {})
    plan = state.get("plan", [])
    reasoning = state.get("reasoning", [])

    primary = intent.get("primary", {})
    intent_name = primary.get("name", "unknown")
    confidence = primary.get("confidence", 0.0)

    action = {
        "type": "guidance",
        "target": None,
        "message": "No direct action selected"
    }

    # High-confidence actions
    if confidence >= 0.75:
        if intent_name == "bridge_funds":
            action = {
                "type": "handoff",
                "target": "bridge_agent",
                "message": "Ready to handoff to Bridge Agent"
            }

        elif intent_name == "risk_check":
            action = {
                "type": "review",
                "target": "risk_agent",
                "message": "Recommend risk review before execution"
            }

        else:
            action = {
                "type": "guidance",
                "target": None,
                "message": "Proceed with planned steps"
            }

    else:
        action = {
            "type": "clarify",
            "target": None,
            "message": "Intent confidence low, need clarification"
        }

    reasoning.append(f"Action decision: {action['type']}")

    return {
        **state,
        "action": action,
        "reasoning": reasoning
    }
