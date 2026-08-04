from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()
model=ChatOpenAI()
parser1=StrOutputParser()

template1 = PromptTemplate(
    template='write the notes of the following topic \n {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='write the quiz of the following topic \n {topic}',
    input_variables=['topic']
)

chain1= RunnableParallel({
    'topic' : template1 | model | parser1,
    'notes' : template2 | model | parser1
}
)

result=chain1.invoke({'topic': 'langchain'})
print(result)