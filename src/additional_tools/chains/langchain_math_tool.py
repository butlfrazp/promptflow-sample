from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

@tool
def langchain_math_chat_tool(chat_prompt, connection: AzureOpenAIConnection) -> str:

    chat_model = AzureChatOpenAI(
        deployment_name='gpt-35-turbo',
        openai_api_version=connection.api_version,
        openai_api_key=connection.api_key,
        openai_api_base=connection.api_base
    )

    reply_message = chat_model([HumanMessage(content=chat_prompt)])
    return reply_message.content