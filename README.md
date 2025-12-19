# 🧠 Warden Task Orchestrator  
> The brain that thinks before you act.

A next-generation **LangGraph-powered Community Agent** built for the Warden ecosystem — designed to understand intent, plan intelligently, and orchestrate complex actions with clarity.

This is not a chatbot.  
This is an **orchestrator**.

---

## 🚀 Why this agent is different

Most agents jump straight to execution.

**Warden Task Orchestrator does something smarter first:**
- It **understands what the user really wants**
- It **breaks the goal into clear, safe, actionable steps**
- It **recommends the right agents or actions**, instead of guessing

Think of it as the **control layer** for all other agents.

---

## 🧩 What can users do with this agent?

Users can ask things like:

- “I want to bridge USDC to Base”
- “How do I move assets safely across chains?”
- “What steps should I follow before interacting with a new protocol?”
- “Which agent should I use for this task?”

And the agent will:
1. Detect the **intent**
2. Build a **step-by-step plan**
3. Recommend **specialized agents or actions**
4. Highlight **risks & checks** before execution

---

## 🛠️ Core Capabilities

### 🎯 Intent Detection
Understands *what* the user is trying to achieve, not just what they typed.

### 🗺️ Intelligent Planning
Converts a goal into a logical, ordered execution plan.

### 🤖 Agent Recommendation
Suggests the most suitable agent (e.g. Bridge Agent, DeFi Agent, etc.).

### 🧠 Graph-based Reasoning
Powered by **LangGraph**, ensuring deterministic, inspectable flows.

### 🔒 Safety-First by Design
No wallet access.  
No state storage.  
Pure orchestration & guidance — aligned with Warden Phase-1 security.

---
## 🔒 Agent Hub Safety & Compliance

This agent is designed to fully comply with Warden Agent Hub Phase-1 rules:

- ❌ No wallet access
- ❌ No private key handling
- ❌ No transaction execution
- ❌ No data storage on Warden infra

All actions are **advisory, simulated, or handed off** to specialized agents.

This agent acts purely as an **orchestration and reasoning layer**.
---

## 🔄 Simple Execution Flow

### 🧪 Example Flow

**Input**

**Output**
- **Intent:** `bridge_funds` (0.90 confidence)
- **Plan:** 3-step execution plan
- **Action:** `handoff → Bridge Agent`

This flow ensures that **no action is executed directly** — only validated recommendations or agent handoffs are produced.

This agent follows a deterministic, safety-first orchestration flow powered by **LangGraph**.

## 🔍 Example Response

```json
{
  "summary": "Detected intent: bridge_funds",
  "confidence": 0.9,
  "recommended_steps": [
    "Select a trusted bridge",
    "Verify destination chain and token support",
    "Review bridge-related risks"
  ],
  "action": {
    "type": "handoff",
    "target": "Bridge Agent",
    "message": "Ready to hand off to Bridge Agent"
  }
}
