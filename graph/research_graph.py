from langgraph.graph import StateGraph
from compression.compressor import compress
from agents.researcher import researcher_agent
from agents.critic import critic_agent
from agents.synthesizer import synthesizer_agent


def build_graph():
    graph = StateGraph(dict)

    # --- Research Node ---
    def research_node(state):
        research_text = researcher_agent(state["topic"])
        return {
            "topic": state["topic"],
            "research": compress(research_text),
        }

    # --- Critique Node ---
    def critique_node(state):
        critique_text = critic_agent(state["research"])
        return {
            "topic": state["topic"],
            "research": state["research"],
            "critique": compress(critique_text),
        }

    # --- Synthesis Node ---
    def synthesize_node(state):
        final_text = synthesizer_agent(
            state["research"],
            state["critique"],
        )
        return {
            "final": final_text
        }

    # Register nodes
    graph.add_node("research", research_node)
    graph.add_node("critique", critique_node)
    graph.add_node("synthesize", synthesize_node)

    # Execution flow
    graph.set_entry_point("research")
    graph.add_edge("research", "critique")
    graph.add_edge("critique", "synthesize")

    return graph.compile()
