#Chatprompttemplate ->list of messages , dynamic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()
llm=ChatOpenAI()
chathistory=[]


template=ChatPromptTemplate.from_messages([ 
    ("system", "Act like a professional"),
    MessagePlaceholder(variable_name='history')
    ("human", "expalin the topic in detail \n {topic}")
])


user_input=input('tell the topic u want to know about')
prompt= template.invoke({'history':chathistory,
                         'topic': user_input})


result=llm.invoke(prompt)
chathistory.append(result)
print(result)