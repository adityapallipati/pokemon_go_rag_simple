# Pokémon Go LLM App

This application leverages large language models (LLMs) to answer questions about Pokémon Go using retrieval-augmented generation (RAG). The app allows you to switch between OpenAI, Hugging Face, and RAG models using your own Pokémon Go dataset.

## Features
- Retrieve detailed Pokémon data such as DPS, movesets, types, and more.
- Ask open-ended questions related to Pokémon Go.
- Supports multiple models: OpenAI GPT, Hugging Face, and RAG (combining retrieval and generation).

---

## Prerequisites

Before starting, ensure you have:

- **Python 3.11+** installed on your system.
- Access to **OpenAI** and **Hugging Face** API keys.

### 1. Get an OpenAI API Key

1. Visit [OpenAI's API page](https://platform.openai.com/signup/).
2. Sign up or log in with your OpenAI account.
3. Navigate to the **API keys** section under your account settings.
4. Create a new API key and copy it.

For more details, see [OpenAI's API Documentation](https://platform.openai.com/docs/).

### 2. Get a Hugging Face API Key

1. Go to [Hugging Face](https://huggingface.co/join) and create or log into your account.
2. Once logged in, go to **Settings** and select **Access Tokens**.
3. Generate a new token and copy it.

For more details, see [Hugging Face API Documentation](https://huggingface.co/docs).

---

## Project Setup

### 1. Set Up a Virtual Environment

To avoid conflicts with global packages, create a Python virtual environment:

```bash
python3 -m venv venv
```

Mac OS/Linux
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

Install Dependencies
```bash
pip install -r requirements.txt
```

Run App:
```bash
cd llm-pokemon-app/src/
streamlit run app.py
```



