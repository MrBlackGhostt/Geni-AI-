from langchain_openai import OpenAI, chat_models

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi there"),
]
model = init_chat_model("gpt-4o-mini", model_provider="openai")

llm = OpenAI()
response = model.invoke(messages)
print(response.content)
