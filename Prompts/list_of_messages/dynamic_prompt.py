from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

template=ChatPromptTemplate([
    {'system':'u are professional {domain}'},
    {'user':'tell me about {topic}'}
    ])

prompt= template.invoke({'domain':'cricket', 'topic':'ball'})

print(prompt)