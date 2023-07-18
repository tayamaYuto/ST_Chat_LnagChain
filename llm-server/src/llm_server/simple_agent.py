from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

def ask_question(question: str) -> str:
    llm = OpenAI(temparature=0.9)
