from pydantic import BaseModel
from typing import List, Optional, TypedDict


class UserRequest(BaseModel):
    query: str


class AgentState(TypedDict, total=False):
    query: str
    intent: Optional[dict]
    plan: Optional[List[str]]
    reasoning: Optional[List[str]]
    decision_path: Optional[List[str]]

class IntentResult(TypedDict):
    name: str
    confidence: float
    reason: str

class MultiIntentResult(TypedDict):
    primary: IntentResult
    secondary: Optional[List[IntentResult]]



class ExplainableOutput(TypedDict):
    query: str
    intent: dict
    reasoning: List[str]
    plan: List[str]
    next_action: str
