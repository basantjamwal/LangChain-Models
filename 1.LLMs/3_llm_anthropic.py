from langchain_anthropic import AnthropicLLM
from dotenv import load_dotenv

load_dotenv()

llm = AnthropicLLM(model_name="claude-3-sonnet")
result = llm.invoke("what is IP means ?")

print(result)