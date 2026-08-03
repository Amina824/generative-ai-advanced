from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

model=ChatOpenAI()

load_dotenv()
parser=StrOutputParser()

prompt=PromptTemplate(
    template='Tell me a joke abot the following topic \n {topic}',
    input_variables=['topic']
)

chain=RunnableSequence(prompt, model, parser)

result=chain.invoke({'topic':'monkeys'})

print(result)