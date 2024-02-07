from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

loader = TextLoader("facts.txt")

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200, 
    chunk_overlap=0
)

docs = loader.load_and_split(text_splitter)   

for doc in docs:
    print(doc.page_content)
    print("\n")