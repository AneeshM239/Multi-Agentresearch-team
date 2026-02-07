from utils.llm import get_llm

def critic_agent(research_text: str) -> str:
    """
    Critic Agent:
    Analyzes the research output to identify gaps,
    weak assumptions, ambiguities, or missing perspectives.
    """
    llm = get_llm()

    prompt = f"""
You are a critical reviewer.

Your task:
- Identify logical gaps, missing context, or weak assumptions
- Point out ambiguities or areas needing clarification
- Highlight potential limitations or risks
- Do NOT add new research
- Do NOT summarize
- Do NOT provide a final conclusion

Research to critique:
{research_text}
"""

    response = llm.invoke(prompt)
    return response.content
