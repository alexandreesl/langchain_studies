from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
def analyze_image(image_url: str, question: str) -> str:
    chat = ChatOpenAI(model="gpt-4o-mini", max_tokens=256)
 
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": question
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                    "detail": "auto"
                }
            }
        ]
    )
 
    response = chat.invoke([message])
    return response.content
# Example usage
# Example usage
image_url = "https://drive.google.com/uc?export=view&id=10QOtWYJYYi7HJYPR4zbZCF7wa5bhJc39"
questions = [
    "What objects do you see in this image?",
    "What is the overall mood or atmosphere?",
    "Are there any people in the image?"
]
for question in questions:
    print(f"\nQ: {question}")
    print(f"A: {analyze_image(image_url, question)}")