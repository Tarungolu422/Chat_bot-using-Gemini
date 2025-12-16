import os
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Google GenAI Key
os.environ["GOOGLE_API_KEY"] = ""  # Add your Gemini key here

# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "Add_your_LangSmith_key_here"
os.environ["LANGCHAIN_PROJECT"] = "My-GenAI-Project-Gemini"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am a chatbot powered by Google Generative AI. Please type your queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LLM - GOOGLE GENAI PROJECT (Gemini Model) - By Tarun")
input_text = st.text_input("How may I help you?")

# Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
