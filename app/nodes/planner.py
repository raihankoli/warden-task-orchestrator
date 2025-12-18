from app.schemas import AgentState

def planner_node(state: AgentState) -> AgentState:
    intent = state["intent"]

    if intent == "bridge_funds":
        plan = [
            "Use the deBridge Agent to move assets across chains",
            "Verify destination chain and token support",
            "Review bridge-related risks before proceeding"
        ]

    elif intent == "find_yield":
        plan = [
            "Explore farming opportunities using Base Farmer",
            "Check TVL and protocol maturity",
            "Understand yield-related risks"
        ]

    elif intent == "swap_tokens":
        plan = [
            "Compare swap routes using Uniswap or Jupiter",
            "Review slippage and fees",
            "Confirm transaction details before swapping"
        ]

    elif intent == "analyze_portfolio":
        plan = [
            "Analyze asset allocation",
            "Identify risk concentration",
            "Adjust strategy based on risk tolerance"
        ]

    else:
        plan = [
            "Clarify your goal",
            "Choose the appropriate Warden agent",
            "Proceed carefully"
        ]

    return {
        **state,
        "plan": plan
      }
