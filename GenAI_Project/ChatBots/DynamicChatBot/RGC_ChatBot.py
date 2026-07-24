from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.5-flash-lite",temperature = 0.5)

st.title("ChatBot with RGC Prompt template")

role = st.selectbox('Select the Ai Role:',['Ai Engineer','Software Developer','Architect','DataAnalyst','Finance Expert'])
goal = st.text_input('What Is the goal of request')
context = st.text_input('What is the context for the AI')
query = st.text_input('What is your query?')

template = PromptTemplate(template="""You are an senior {role} working in a company. You always have a gaol in mind that is {goal}, 
with context {context}, and this is the Questions {query}. """,input_variables=['role','goal','context','query'],validate_template=True)

final_prompt = template.invoke({'role':role,'goal':goal,'context':context,'query':query})

answer = model.invoke(final_prompt)

if st.button('Answer'):
    st.write(answer)







