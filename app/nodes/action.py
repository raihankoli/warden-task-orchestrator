from app.schemas import AgentState

def action_router_node(state: AgentState) -> AgentState:
    intent = state.get("intent", {})
    plan = state.get("plan", [])
    reasoning = state.get("reasoning", [])

    primary = intent.get("primary", {})
    intent_name = primary.get("name", "unknown")
    confidence = primary.get("confidence", 0.0)

    action = {
        "type": "inform",
        "target": None
    }

    if intent_name == "bridge_funds" and confidence >= 0.75:
        action = {
            "type": "handoff",
            "target": "bridge_agent"
        }

    elif intent_name == "risk_check":
        action = {
            "type": "handoff",
            "target": "risk_agent"
        }

    elif confidence < 0.75:
        action = {
            "type": "confirm",
            "target": None
        }

    reasoning.append(f"Action decided: {action['type']}")

    return {
        **state,
        "action": action,
        "reasoning": reasoning
  }
