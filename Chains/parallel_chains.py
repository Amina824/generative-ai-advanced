from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()
model=ChatOpenAI()
parser = StrOutputParser()

template1 = PromptTemplate(
    template=("give me the notes of the following topic \n {topic}"),
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = ("give me the quiz of the following topic \n {topic}"), 
    input_variables = ['topic']
)

chain = RunnableParallel({
    'Notes': template1 | model | parser,
    'Quiz': template2 | model | parser,
})

user_input=input("tell me he topic u want to khave quiz and notes:")

result = chain.invoke({'topic': user_input})

print( result )