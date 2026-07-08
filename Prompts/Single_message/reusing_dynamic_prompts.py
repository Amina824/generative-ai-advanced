from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model=ChatOpenAI()

input_topic= st.selectbox("Select the topic", ["AI","Machine learning", "deep learning","reinforcement learning"])

input_length=st.selectbox("choose the length",["1-2 lines","2-3 lines"," 3-4 lines"])

input_tone=st.selectbox("Choose the tone", ["fun","professional","user-friendly"])




template=load_prompt('template.json')

prompt=template.invoke({
    'input_topic':input_topic,
    'input_length':input_length,
    'input_tone':input_tone })

if st.button('Summarize'):
    result=model.invoke(prompt)
    st.write(result.content)