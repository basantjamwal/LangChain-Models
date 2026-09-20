from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name="claude-3-sonnet")
result = model.invoke("hy")

print(result)