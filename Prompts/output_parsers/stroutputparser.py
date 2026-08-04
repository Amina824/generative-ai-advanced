from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI()
parser=StrOutputParser()

prompt=PromptTemplate(
    template='write short explanation of the following topic \n {topic}',
    input_variables=['topic']
)

chain = prompt | model | parser

result = chain.invoke({'topic': 'Pakistan'})
print(result)