from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

parser=JsonOutputParser()

template=PromptTemplate(
    template='Write a detailed report on {topic} \n  {format_instructions}' ,
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()})

chain=template|model|parser

res=chain.invoke({'topic':'black hole'})
print(res)