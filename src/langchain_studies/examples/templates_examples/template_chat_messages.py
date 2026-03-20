from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI

template = ChatPromptTemplate.from_messages([
('system', '''Answer the question based on the context below
If the question cannot be answered using the information provided, answer with "I don't know".'''),
('human', 'Context: {context}'),
('human', 'Question: {question}'),
])

def main() -> None:
    result = template.invoke({
        "context": """The most recent advancements in NLP are bei
Language Models (LLMs). These models outperform their
counterparts and have become invaluable for developer
applications with NLP capabilities. Developers can ta
models through Hugging Face's `transformers` library,
OpenAI and Cohere's offerings through the `openai` alibraries, respectively.""",
        "question": "Which model providers offer LLMs?"
    })
    model = ChatOpenAI()
    response = model.invoke(result)
    print(response)


if __name__ == "__main__":
    main()