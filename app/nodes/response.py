from app.schemas import AgentState

def response_node(state: AgentState) -> dict:
    intent = state.get("intent", {})
    plan = state.get("plan", []) or []
    reasoning = state.get("reasoning", []) or []

    primary_intent = intent.get("primary", {}).get("name", "unknown")

    if primary_intent == "bridge_funds":
        next_action = "Ready to handoff to Bridge Agent"
    elif primary_intent == "risk_check":
        next_action = "Recommend safety review before execution"
    else:
        next_action = "Awaiting clearer user intent"

    return {
        "query": state.get("query"),
        "intent": intent,
        "reasoning": reasoning,
        "plan": plan,
        "next_action": next_action
  }
