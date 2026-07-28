from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite",temperature = 0.5)
domain = input("Domain: ")
query = input("Query: ")

messages = ChatPromptTemplate.from_messages([(
    'system',f''' You are expert in this {domain}, and helping people from long time.'''
),
    ('human','Help me with {query}, in less than 50 words')
])

prompt = messages.invoke({'domain': domain, 'query': query})

responce = model.invoke(prompt)

print(responce.content)