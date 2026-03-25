from langchain_openai import OpenAI
# For factual, consistent responses
factual_llm = OpenAI(temperature=0.1, max_tokens=256)
# For creative brainstorming
creative_llm = OpenAI(temperature=0.8, top_p=0.95, max_tokens=512)


response = factual_llm.invoke('how many eggs does it make a omelet?')
print(response)
print('=======================')
response = creative_llm.invoke('how many eggs does it make a omelet?')
print(response)