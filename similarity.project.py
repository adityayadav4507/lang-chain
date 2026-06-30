from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

docs = [
    "Virat Kohli is an Indian cricketer.",
    "Abhishek Sharma is a cricketer.",
    "Lionel Messi is a footballer."
]

query = "Who is Virat Kohli?"

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",output_dimensionality=5
)

doc_vectors = embedding.embed_documents(docs)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector], doc_vectors)
print("score= ",scores)


for doc, score in zip(docs, scores[0]):
    print(f"{score:.4f} -> {doc}")