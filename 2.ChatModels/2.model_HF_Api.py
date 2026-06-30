from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

model=HuggingFaceEndpoint(repo_id="LiquidAI/LFM2.5-230M")
print(model.invoke("capital of india "))