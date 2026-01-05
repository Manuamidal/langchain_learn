from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

class Report(BaseModel):
     
     name:str=Field(description="name of the person")
     age:int=Field(gt=18,description="age of the person, must be greater than 18")
     city:str=Field(description="city where the person lives")

parser=PydanticOutputParser(pydantic_object=Report)

template=PromptTemplate(
    template='Generate the name,age,city of a fictional {place} person. \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()})

chain=template|model|parser

res=chain.invoke({'place':'New York'})
print(res)
