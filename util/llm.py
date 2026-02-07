from langchain_community.chat_models import ChatOllama

def get_llm():
    return ChatOllama(
        model="llama3.1:8b",
        temperature=0.2
    )
