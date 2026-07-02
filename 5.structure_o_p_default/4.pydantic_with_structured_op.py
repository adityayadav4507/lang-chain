from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,EmailStr,Field
from typing import Optional,Annotated
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review2(BaseModel):
    summary: str = Field(description="write a product review in 10 words")
    sentiment: str = Field(description="write an sentiment in 1 word")
    pos: Optional[list[str]] = Field(description="list of positive points")

structured_model_2=model.with_structured_output(Review2)
result=structured_model_2.invoke(
    """ e iPhone 6s is a well-built and reliable device for basic use, but it is no longer a good choice as a primary smartphone for most people. If you already own one, it can still serve as a backup phone or for light everyday tasks, but buyers looking for a daily driver should consider a newer model."""
)

print(result)
