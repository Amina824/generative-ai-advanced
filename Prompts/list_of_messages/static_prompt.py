from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chathistory=[]

chathistory.append( SystemMessage(content="You are helpful ai assistant"))


while True:
    userinput = input("Ask anything")
    chathistory.append(HumanMessage(content=userinput))
    if userinput == "exit":
        break
    result= model.invoke(chathistory)
    chathistory.append(AIMessage(content=result.content))
    print("AI:", result.content)

    
