from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

class Review(BaseModel):

    sentiment:Literal["positive","negative"]=Field(description="The sentiment of the Review")

parser=PydanticOutputParser(pydantic_object=Review)

template=PromptTemplate(
    template='Classify the sentiment of the following review as positive or negative {topic} \n {format_instructions}' ,
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()})

template1=PromptTemplate(
    template='Write a response for positive review: {review}' ,
    input_variables=['review'])

template2=PromptTemplate(
    template='Write a response for negative review: {review}' ,
    input_variables=['review'])

parser2=StrOutputParser()    

run_chain=template|model|parser

br_chain=RunnableBranch(
    (lambda x: x.sentiment=="positive",  template1 | model | parser2),
    (lambda x: x.sentiment=="negative",  template2 | model | parser2),
    RunnableLambda(lambda x: "No sentiment detected")
)

chain=run_chain|br_chain
res=chain.invoke({'topic':'The movie is very bad and boring'})
print(res)
chain.get_graph().print_ascii()

