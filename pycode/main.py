from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

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

test_prompt = PromptTemplate(
    template="Write a code test for the following {language} code:\n {code}",
    input_variables=["code"]
)

code_chain = LLMChain(
    llm=llm, 
    prompt=code_prompt,
    output_key="code"
)

test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

chain = SequentialChain(
    chains=[code_chain, test_chain], 
    input_variables=["language","task"], 
    output_variables=["code","test"]
)

result = chain({
    "language":args.language, 
    "task":args.task
})

print("GENERATED CODE>>>>>")
print(result["code"])

print("GENERATED TEST>>>>>")
print(result["test"])