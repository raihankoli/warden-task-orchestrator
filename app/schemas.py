
from pydantic import BaseModel
from typing import List, Optional, TypedDict

class UserRequest(BaseModel):
    query: str

class AgentState(TypedDict):
    query: str
    intent: Optional[str]
    plan: Optional[List[str]]
