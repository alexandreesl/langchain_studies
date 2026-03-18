import os
from langchain_openai.llms import OpenAI


def main() -> None:
    model = OpenAI(model="gpt-3.5-turbo-instruct")
    response = model.invoke("It finally happened. I have finished my first LangChain project.")
    print(response)


if __name__ == "__main__":
    main()

