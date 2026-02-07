from utils.llm import get_llm

def researcher_agent(topic: str) -> str:
    """
    Researcher Agent:
    Gathers factual, neutral information about the topic.
    Avoids opinions, conclusions, or recommendations.
    """
    llm = get_llm()

    prompt = f"""
You are a research agent.

Your task:
- Collect factual, neutral, and well-structured information
- Cover key concepts, background, and important points
- Do NOT provide conclusions or opinions
- Do NOT critique or judge

Topic:
{topic}
"""

    response = llm.invoke(prompt)
    return response.content
