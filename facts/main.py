from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

load_dotenv()

embeddings = OpenAIEmbeddings()

loader = TextLoader("facts.txt")

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200, 
    chunk_overlap=0
)

docs = loader.load_and_split(text_splitter=text_splitter)   

db = Chroma.from_documents(docs, 
                           embeddings, 
                           persist_directory="emb")

results = db.similarity_search("what is an interesting fact about the english language", k=2)

for result in results:
    print("\n")
    print(result.page_content)