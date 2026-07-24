import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

#Loading env
load_dotenv()

#laod model
llm = ChatOllama(model='llama3.1:8b',temperature=0.5)

st.title("LLama3.2 7B ChatBot")
st.header("First Chat Bot - Yash")

input_text = st.text_input("Ask ?")

if input_text:
    response = llm.invoke(input_text)
    st.write(response.content)


