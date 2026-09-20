from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = AzureChatOpenAI(model="gpt-4-deployment")
result = model.invoke("hy")

print(result)