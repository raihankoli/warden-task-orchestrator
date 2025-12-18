from app.schemas import AgentState

def intent_node(state: AgentState) -> AgentState:
    query = state["query"].lower()

    if "bridge" in query:
        intent = "bridge_funds"
    elif "farm" in query or "yield" in query:
        intent = "find_yield"
    elif "swap" in query:
        intent = "swap_tokens"
    elif "portfolio" in query or "risk" in query:
        intent = "analyze_portfolio"
    else:
        intent = "general_guidance"

    return {
        **state,
        "intent": intent
  }
