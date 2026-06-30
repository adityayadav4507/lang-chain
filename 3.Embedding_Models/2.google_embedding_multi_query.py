from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",output_dimensionality=5)
doc=["what is india",
     "what is capital of india ",
     "whats is cricket"]
result=embedding.embed_documents(doc)
print(result)