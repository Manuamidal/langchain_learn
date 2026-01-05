import langchain
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
embeddings=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",output_dimensionality=32)
response=embeddings.embed_query("what is the capital of India")
print(response)