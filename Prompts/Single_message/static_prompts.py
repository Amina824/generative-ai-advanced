from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-4',temperature=1, max_completion_tokens=20)
result=model.invoke("tell me about pakistan in few words")
print(result.content)
print(result)



