from langchain_openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = AzureOpenAI(model="gpt-4")
result = llm.invoke("what is GST")

print(result)