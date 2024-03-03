from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv



load_dotenv()


chat = ChatOpenAI(streaming=True
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

class StreamableChain:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            self(input, callbacks=[handler]) #running the chain, using it's own handler

        Thread(target=task).start()
        
        while True:
            token = queue.get()
            if token is None:
                break
            yield token

class StreamingChain(StreamableChain, LLMChain):
    pass

chain = StreamingChain(llm=chat, prompt=prompt)

for output in chain.stream(input={"content": "tell me a joke"}):
    print(output)