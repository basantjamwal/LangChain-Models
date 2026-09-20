from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs = [
    "hello ",
    "nice to meet you",
    "welcome"
]

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2" , output_dimensionality=10)
result = embedding.embed_documents(docs)

print(result)