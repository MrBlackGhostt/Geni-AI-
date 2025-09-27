import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import textwrap
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GOOGLE_GEMINI_KEY")


genai.configure(api_key=key)
model = ChatGoogleGenerativeAI(model="gemini-pro")

res = model.invoke("hello")

print(res.content)
