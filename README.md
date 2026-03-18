# LangChain Studies

A Python project for studying and experimenting with [LangChain](https://python.langchain.com/).

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. **Install `uv`** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies for this project**:
   ```bash
   uv sync
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
uv run python -m langchain_studies.your_script
```

Or run directly inside the project’s environment:

```bash
python -m langchain_studies.your_script
```

## Environment variables

For OpenAI and other API keys, use a `.env` file in the project root (add `.env` to `.gitignore`). Example:

```
OPENAI_API_KEY=sk-...
```
