from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

template=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic'])

template2=PromptTemplate(
    template='Summarize the following text in 5 lines:\n\n{text}',
    input_variables=['text'])

parser=StrOutputParser()

chain=template|model|parser|template2|model|parser

res=chain.invoke({'topic':'black hole'})
print(res)