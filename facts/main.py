from dotenv import load_dotenv
from langchain.document_loaders import TextLoader

load_dotenv()

loader = TextLoader("facts.txt")

docs = loader.load()   
print(docs)