from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

template=PromptTemplate(
    template='Write a detailed report on {topic}' ,
    input_variables=['topic'])

parser=StrOutputParser()

chain=template|model|parser

#res=chain.invoke({'topic':'black hole'})
#print(res)
chain.get_graph().print_ascii()