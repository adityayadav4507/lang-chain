from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() # load the api key 
model_1=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model_1.invoke("what is capital of india")
print("responce = ", result)

print("content only Res = ",result.content)