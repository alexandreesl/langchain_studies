from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


def main() -> None:
    model = ChatOpenAI()
    system_msg = SystemMessage(
        '''Answer the question based on the context below. If the quest
answered using the information provided, answer with "I don't know."
            Context: The most recent advancements in NLP are being drive by large language models (LLMs).
These models outperform their smaller counter
become invaluable for developers who are creating applicatio
capabilities. Developers can tap into these models through the `transformers` library, or by utilizing OpenAI and Cohere's
libraries, respectively.
        '''
        )

    human_msg = HumanMessage('Which model providers offer LLMs?')
    response = model.invoke([system_msg, human_msg])
    print(response.content)


if __name__ == "__main__":
    main()