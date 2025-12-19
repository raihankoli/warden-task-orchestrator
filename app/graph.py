from langgraph.graph import StateGraph, END
from app.schemas import AgentState
from app.nodes.intent import detect_intent
from app.nodes.planner import build_plan

CONFIDENCE_THRESHOLD = 0.75


def intent_node(state: AgentState) -> AgentState:
    result = detect_intent(state["query"])
    return {
        **state,
        "intent": result
    }


def confidence_router(state: AgentState) -> str:
    primary_conf = state["intent"]["primary"]["confidence"]

    if primary_conf >= CONFIDENCE_THRESHOLD:
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

    graph.set_entry_point("intent")

    graph.add_conditional_edges(
        "intent",
        confidence_router,
        {
            "plan": "plan",
            "clarify": "clarify"
        }
    )

    graph.add_edge("plan", END)
    graph.add_edge("clarify", END)

    return graph.compile()
