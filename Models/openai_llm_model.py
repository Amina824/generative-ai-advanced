from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

modelllm= OpenAI()

result=modelllm.invoke("Tell me the capital city of Pakistan")
print(result)