from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from promptflow import tool
from promptflow.connections import AzureOpenAIConnection


@tool(
    name="langchain_chain",
    description="This is langchain_chain tool",
)
def langchain_chain(
    connection: AzureOpenAIConnection,
    deployment_name: str,
    chat_prompt: str) -> str:
    llm = AzureChatOpenAI(
        deployment_name=deployment_name,
        openai_api_version=connection.api_version,
        azure_endpoint=connection.api_base,
        openai_api_key=connection.api_key,
    )

    messages = [
        HumanMessage(content=chat_prompt),
    ]

    return llm(messages).content
