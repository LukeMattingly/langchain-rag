from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from redundant_filter_retriever import RedundantFilterRetriever
import langchain

langchain.debug = True
load_dotenv()

chat = ChatOpenAI()

embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings, 
)

retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db,
)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff",
)

result = chain.run("tell me a fact abou the original star spangled banner")
print(result)