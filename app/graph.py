from langgraph.graph import StateGraph, END
from app.schemas import AgentState
from app.nodes.intent import detect_intent
from app.nodes.planner import build_plan
from app.nodes.response import response_node
from app.nodes.action import action_router_node

CONFIDENCE_THRESHOLD = 0.75


def intent_node(state: AgentState) -> AgentState:
    result = detect_intent(state["query"])

    reasoning = []
    primary = result.get("primary", {})

    reasoning.append(
        f"Detected primary intent: {primary['name']} "
        f"(confidence {primary['confidence']})"
    )

    for sec in result.get("secondary", []):
        reasoning.append(f"Detected secondary intent: {sec['name']}")

    if primary["confidence"] < CONFIDENCE_THRESHOLD:
        reasoning.append("Confidence below threshold — clarification required")
    else:
        reasoning.append("High confidence intent — proceeding to planning")

    return {
        **state,
        "intent": result,
        "reasoning": reasoning
    }


def confidence_router(state: AgentState) -> str:
    intent = state.get("intent") or {}
    primary = intent.get("primary") or {}
    confidence = primary.get("confidence", 0.0)

    if confidence >= CONFIDENCE_THRESHOLD:
        return "plan"
    return "clarify"


def clarify_node(state: AgentState) -> AgentState:
    return {
        **state,
        "plan": [
            "Ask the user to clarify their goal",
            "Request missing details before proceeding"
        ]
    }


def planner_node(state: AgentState) -> AgentState:
    plan = build_plan(state["intent"])
    return {
        **state,
        "plan": plan
    }


def build_graph():
    graph = StateGraph(AgentState)

graph.add_node("intent", intent_node)
graph.add_node("clarify", clarify_node)
graph.add_node("plan", planner_node)
graph.add_node("action", action_router_node)
graph.add_node("response", response_node)

graph.set_entry_point("intent")

graph.add_conditional_edges(
    "intent",
    confidence_router,
    {
        "plan": "plan",
        "clarify": "clarify"
    }
)

graph.add_edge("plan", "action")
graph.add_edge("clarify", "action")
graph.add_edge("action", "response")
graph.add_edge("response", END)

return graph.compile()
