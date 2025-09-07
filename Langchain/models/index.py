from langchain_openai import OpenAI, chat_models

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate

model = init_chat_model("gpt-4o-mini", model_provider="openai")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate(
    [
        ("system", "You are an ai assistant name is {name}"),
        ("human", "Hello, how are you doing"),
        ("ai", "I am doing well"),
        ("human", "{user_input}"),
    ]
)

# print(
#     prompt_template.invoke(
#         {"name": "Bob", "user_input": "Why the rocket go horizontally when go up"}
#     )
# )

# print(
#     prompt_template.format_message(
#         {"name": "Bob", "user_input": "Why the rocket go horizontally when go up"}
#     )
# )

print(
    model.invoke(
        prompt_template.invoke(
            {"name": "Bob", "user_input": "Why the rocket go horizontally when go up"}
        )
    )
)

# prompt = prompt_template.invoke({"language": "Italin", "text": "hi"})

# print(prompt_template)
# print(
#     model.invoke(
#         [
#             HumanMessage(content="Hi! I'm Bob"),
#             AIMessage(content="Hello Bob! How can I assist you today?"),
#             HumanMessage(content="What's my name?"),
#         ]
#     )
# )
