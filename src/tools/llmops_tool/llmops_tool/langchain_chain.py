from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from promptflow import tool
from promptflow.connections import AzureOpenAIConnection


@tool(
    name="langchain_chain",
    description="This is langchain_chain tool",
)
def langchain_chain(
    connection: AzureOpenAIConnection,
    deployment_name: str,
    system_message: str,
    query: str) -> str:
    llm = AzureChatOpenAI(
        deployment_name=deployment_name,
        openai_api_version=connection.api_version,
        azure_endpoint=connection.api_base,
        openai_api_key=connection.api_key,
    )

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=query),
    ]

    return llm(messages).content
