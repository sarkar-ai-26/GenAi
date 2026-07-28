from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite",temperature = 0.5)

query =input(print("Ask query? : "))

messages = [SystemMessage(content=''' You are a helpful asssistant to guide a student in becoming software developer
'''), HumanMessage(content=query)]

response = llm.invoke(messages)

print(AIMessage(content= response.content))