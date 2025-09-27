from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
import os
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI

messages = [
    SystemMessage("You are a friendly dietician."),
    HumanMessage("What is a balanced meal plan for weight loss?"),
]


# llm = GoogleGenerativeAI(
#     model="gemini-2.5-pro", google_api_key="AIzaSyC77SYkbWAQFkZbrJyMc_Gwh3bfVJNW514"
# )
llm = ChatOpenAI()
res = llm(messages)
print(res)
