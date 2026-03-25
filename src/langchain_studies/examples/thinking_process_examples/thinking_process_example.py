from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a problem-solving assistant."),
    ("user", "{problem}")
])
# Initialize with reasoning_effort parameter
chat = ChatOpenAI(
    model="o3-mini",
    reasoning_effort="high"  # Options: "low", "medium", "high"
)
chain = template | chat
response = chain.invoke({"problem": "Calculate the optimal strategy for creating a house"})
print(response)
print('=====================================')
chat = ChatOpenAI(model="gpt-4o")
chain = template | chat
response = chain.invoke({"problem": "Calculate the optimal strategy for creating a house"})
print(response)