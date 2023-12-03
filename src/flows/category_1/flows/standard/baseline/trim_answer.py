from promptflow import tool

@tool
def trim_answer(answer: str) -> str:
    return answer.strip()
