from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatOpenAI()
parser = StrOutputParser()

template=PromptTemplate(
    template=("tell me 5 lines about the following topic \n {topic}"),
    input_variables=['topic']
)
user_input=input("tell me he topic u want to know about:")

chain= template | model | parser

result = chain.invoke({'topic' : user_input})

print( result )

