from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','you are the {domain} expert'),
    ('human','explain the  {query}'),
])

prompt=chat_template.invoke({'domain':'math','query':'cricle'})

print(prompt)