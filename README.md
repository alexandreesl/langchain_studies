# LangChain Studies

A Python project for studying and experimenting with [LangChain](https://python.langchain.com/).

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Create and activate the virtual environment, then install dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the shell** (optional):
   ```bash
   poetry shell
   ```

## Installed packages

- **langchain** – Core LangChain framework
- **langchain-openai** – OpenAI integrations (ChatGPT, embeddings, etc.)
- **langchain-community** – Community integrations and utilities
- **langchain-text-splitters** – Text splitting for RAG and chunking
- **langchain-postgres** – PostgreSQL vector store and persistence

## Usage

Run scripts from the project root:

```bash
poetry run python -m langchain_studies.your_script
```

Or after `poetry shell`:

```bash
python -m langchain_studies.your_script
```

## Environment variables

For OpenAI and other API keys, use a `.env` file in the project root (add `.env` to `.gitignore`). Example:

```
OPENAI_API_KEY=sk-...
```
