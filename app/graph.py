from langgraph.graph import StateGraph, END
from app.schemas import AgentState
from app.nodes.intent import intent_node
from app.nodes.planner import planner_node

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", intent_node)
    graph.add_node("planner", planner_node)

    graph.set_entry_point("intent")
    graph.add_edge("intent", "planner")
    graph.add_edge("planner", END)

    return graph.compile()

graph = build_graph()

def run_graph(query: str):
    result = graph.invoke({
        "query": query,
        "intent": None,
        "plan": None
    })

    return {
        "query": query,
        "detected_intent": result["intent"],
        "plan": result["plan"]
    }
