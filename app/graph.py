from langgraph.graph import StateGraph, END
from app.schemas import AgentState
from app.nodes.intent import detect_intent
from app.nodes.planner import build_plan

CONFIDENCE_THRESHOLD = 0.75


def intent_node(state: AgentState) -> AgentState:
    result = detect_intent(state["query"])

    reasoning = []
    primary = result["primary"]

    reasoning.append(
        f"Detected primary intent: {primary['name']} "
        f"(confidence {primary['confidence']})"
    )

    if result.get("secondary"):
        for sec in result["secondary"]:
            reasoning.append(
                f"Detected secondary intent: {sec['name']}"
            )

    if primary["confidence"] < CONFIDENCE_THRESHOLD:
        reasoning.append(
            "Confidence below threshold — clarification required"
        )
    else:
        reasoning.append(
            "High confidence intent — proceeding to planning"
        )

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


}

 def planner_nstate: AgentStatet -> AgentState:
    plan = n = build_pstatetate["inten
        re u
          state,
            "p: plan
     


}

 def build_gra:
    graph = h = StateGrAgentStatet

    graph.aph.add_node("int, intent_noden
    graph.aph.add_node("clar, clarify_noden
    graph.aph.add_node("p, planner_noden

    graph.aph.set_entry_point("inte

    graph.aph.add_conditional_ed
            "int,
        confidence_router,
         
                "p: n": "p,
                "clar: y": "clar
         
     

    graph.aph.add_edge("p, END 
    graph.aph.add_edge("clar, END 

        re graph.aph.compi
