from langchain_core.prompts import PromptTemplate
from langchain_openai.llms import OpenAI

template = PromptTemplate.from_template("""Answer the question based on the context below. 
If the question cannot be answered using the provided context, answer with "I don't know".
Context: {context}
Question: {question}
Answer: """)

def main() -> None:
    result = template.invoke({
        "context": """The most recent advancements in NLP are being driven by Large Language Models (LLMs).
These models outperform their
counterparts and have become invaluable for developer
applications with NLP capabilities. Developers can take
models through Hugging Face's `transformers` library,
OpenAI and Cohere's offerings through the `openai` an
libraries, respectively.""",
        "question": "Which model providers offer LLMs?"
    })
    model = OpenAI()
    response = model.invoke(result)
    print(response)


if __name__ == "__main__":
    main()