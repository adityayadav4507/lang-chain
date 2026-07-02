from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict,Annotated
from dotenv import load_dotenv

load_dotenv()

class Review1(TypedDict):
    summary:str
    sentiment:str


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_model=model.with_structured_output(Review1) ## this generate system prompt 

result=structured_model.invoke(
    """iPhone 6s is a well-built and reliable device for basic use, but it is no longer a good choice as a primary smartphone for most people. If you already own one, it can still serve as a backup phone or for light everyday tasks, but buyers looking for a daily driver should consider a newer model. """
)

print(result)

## it may be possible model can not understand the keyword
## or to give extra info 


class Review2(TypedDict):
    summary: Annotated[str, "write a product review in 10 words"]
    sentiment: Annotated[str, "write an sentiment in 1 word"]

structured_model_2=model.with_structured_output(Review2)
result=structured_model_2.invoke(
    """ e iPhone 6s is a well-built and reliable device for basic use, but it is no longer a good choice as a primary smartphone for most people. If you already own one, it can still serve as a backup phone or for light everyday tasks, but buyers looking for a daily driver should consider a newer model."""
)

print(result.keys())
