from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

template1=PromptTemplate(
    template='Write a joke on {topic}' ,
    input_variables=['topic'])

template2=PromptTemplate(
    template='explain the {joke} in detail' ,
    input_variables=['joke'])
parser=StrOutputParser()

jo_chain=template1|model|parser

run_chain=RunnableParallel({
    "joke_chain":RunnablePassthrough(),
    "explain_chain":template2|model|parser
})

chain=jo_chain|run_chain

res=chain.invoke({'topic':'black hole'})
print(res)

chain.get_graph().print_ascii()



