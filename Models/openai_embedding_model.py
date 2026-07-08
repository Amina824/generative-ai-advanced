from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

query="Today,I am learning langchain"
document=["Lanchain is open source framwork."  ,
          "It is used to run the apps powered by ai",
          "there are various reasons of using it",
          "provides mind,pipline for automation and apis"]              

model= OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

query_result = model.embed_query(query)
doc_result = model.embed_documents(document)

print(query_result)
print("this is doc embeddings result", doc_result)