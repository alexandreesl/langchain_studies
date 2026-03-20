from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
# Initialize OpenAI model
openai_llm = OpenAI()
# Initialize a Gemini model
gemini_pro = GoogleGenerativeAI(model="gemini-flash-latest")
# Either one or both can be used with the same interface
response = openai_llm.invoke("Tell me a joke about light bulbs!")
google_resppnse = gemini_pro.invoke("Tell me a joke about light bulbs!")
print(response)
print('==============================')
print(google_resppnse)

