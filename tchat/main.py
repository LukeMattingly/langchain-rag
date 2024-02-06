from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory, ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(verbose=True)


memory = ConversationSummaryMemory(
    #chat_memory=FileChatMessageHistory(file_path="messages.json"),
    memory_key="messages", 
    return_messages=True, 
    llm=chat
)

prompt = ChatPromptTemplate(
    input_variables = ["content", "messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True,
)


while True:
    try:
        content = input(">> ")
        result = chain({"content":content})
        print(result['text'])    
    except:
        break