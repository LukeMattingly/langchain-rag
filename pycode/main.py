from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('--language', type=str, default='Python')
parser.add_argument('--task', type=str, default='add two numbers')
args = parser.parse_args()

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"],
    
)

code_chain = LLMChain(
    llm=llm, 
    prompt=code_prompt
)

result = code_chain.run(language=args.language, task=args.task)

print(result)