from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch , RunnableLambda
from typing import Literal
from pydantic import BaseModel, Field

load_dotenv()
model=ChatOpenAI()
parser1=StrOutputParser()


class Review(BaseModel):
    sentiment:Literal['positive', 'negative']=Field(description='give the sentiment of the review')

parser2=PydanticOutputParser(pydantic_object=Review)

template1= PromptTemplate(
    template='tell whether the following review is positive or negative \n {review} \n {instructions}',
    input_variables=['review'],
    partial_variables={'instructions': parser2.get_format_instructions()}
)

template2= PromptTemplate(
    template='write a response if a review is positive \n {feedback}',
    input_variables=['feedback']
)

template3= PromptTemplate(
    template='write a response if a review is negative\n {feedback}',
    input_variables=['feedback']
)

chain1 = template1 | model | parser2


chain2= RunnableBranch(
    (lambda x:x.sentiment=='positive', template2|model|parser1),
    (lambda x:x['sentiment']=='negative', template3|model|parser1),
    RunnableLambda(lambda x: 'Rview is neither positive nor negative')
)

final_chain=chain1 |chain2

result= final_chain.invoke({'review':'what a nice phone it is'})
print(result)