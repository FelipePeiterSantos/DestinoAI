import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

tools = load_tools(['ddg-search','wikipedia'], llm = llm)

#result = llm.invoke("Write a ballad about LangChain")
#print(result.content)