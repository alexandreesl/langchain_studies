import base64
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.messages.human import HumanMessage
with open("image.png", 'rb') as image_file:
    image_bytes = image_file.read()
    base64_bytes = base64.b64encode(image_bytes).decode("utf-8")
prompt = [
   {"type": "text", "text": "Describe the image: "},
   {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_bytes}"}},
]
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest")
response = llm.invoke([HumanMessage(content=prompt)])
print(response.content)