from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta" ,
    task="text-generation",
    temperature=1.5 ,
)

result = llm.invoke("hy! who made u ?")

print(result)