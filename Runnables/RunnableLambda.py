from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnableBranch, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model=ChatOpenAI()
load_dotenv()
parser=StrOutputParser()

def word_count(text):
    return len(text.split())


template1=PromptTemplate(
    template= 'give short note of the following topic \n {topic}',
    input_variables=['topic']
)

chain1 = template1 | model | parser

chain2= RunnableParallel({
    'notes': RunnablePassthrough(),
    'Total_charachters': RunnableLambda(word_count)
})

final_chain= chain1 | chain2
result = final_chain.invoke({'topic': 'cricket'})
print(result)