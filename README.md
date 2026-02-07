# Multi-Agentresearch-team

A collaborative multi-agent AI system designed to perform deep research by coordinating specialized agents using compressed context sharing.  
The system demonstrates how multi-agent architectures outperform single-agent approaches in research quality, scalability, and token efficiency.

---

##  Overview

Traditional LLM-based research systems rely on a single model instance to gather, reason, and summarize information. This approach suffers from:
- Limited context windows
- Hallucinations due to lack of internal critique
- High token costs for large research scopes

This project addresses these limitations by implementing a **multi-agent research team** where agents collaborate, critique, and synthesize knowledge using **compressed shared context**.

---

##  System Architecture

The system consists of three core agents orchestrated using **LangGraph**:

### 1. Researcher Agent
- Collects factual, neutral information on a given topic
- Focuses on breadth and coverage
- Avoids conclusions or opinions

### 2. Critic Agent
- Reviews the researcher’s output
- Identifies logical gaps, weak assumptions, and missing perspectives
- Acts as an internal validation mechanism

### 3. Synthesizer Agent
- Reconciles research and critique
- Produces a final, structured research summary
- Includes only claims that survive critical evaluation

To enable scalability, all inter-agent communication passes through a **context compression layer**, simulating ScaleDown-style prompt compression.

---

##  Key Features

- Multi-agent coordination using LangGraph
- Context compression to reduce token usage
- Clear separation of agent responsibilities
- Deterministic orchestration flow
- Extensible architecture for additional agents
- Suitable for large-scope research tasks

---

##  Project Structure
