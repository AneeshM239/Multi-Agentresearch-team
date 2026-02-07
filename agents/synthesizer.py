from utils.llm import get_llm

def synthesizer_agent(research_text: str, critique_text: str) -> str:
    """
    Synthesizer Agent:
    Produces a final, structured research output by
    reconciling research findings with critique.
    Only retains claims that survive criticism.
    """
    llm = get_llm()

    prompt = f"""
You are a synthesis agent.

Your task:
- Produce a clear, structured research summary
- Include only claims that survive the critique
- Resolve conflicts between research and critique
- Be precise and cautious
- Do NOT invent new facts
- Do NOT ignore criticism

Research:
{research_text}

Critique:
{critique_text}

Output a well-structured final research summary.
"""

    response = llm.invoke(prompt)
    return response.content
