from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

json_schema={
    "type": "object",
    "description": "A product review with summary, sentiment, and positive points",
    "type":"object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "write a product review in 10 words"
        },
        "sentiment": {
            "type": "string",
            "description": "write an sentiment in 1 word"
        },
        "pos": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "list of positive points"
        }
    },
    "required": ["summary", "sentiment"]
}
structured_model_2=model.with_structured_output(json_schema)
result=structured_model_2.invoke(
    """iPhone 6s is a well-built and reliable device for basic use, but it is no longer a good choice as a primary smartphone for most people. If you already own one, it can still serve as a backup phone or for light everyday tasks, but buyers looking for a daily driver should consider a newer model.""")

print(result)