import tiktoken

def compress(text: str, max_tokens: int = 300) -> str:
    """
    Compress text by truncating to a maximum number of tokens.
    This simulates ScaleDown-style context compression to
    control token usage between agents.
    """
    if not text or not isinstance(text, str):
        return ""

    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    if len(tokens) <= max_tokens:
        return text

    compressed_tokens = tokens[:max_tokens]
    compressed_text = encoding.decode(compressed_tokens)

    return compressed_text
