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

### This simple llm app highlights the difference between large language models and showcases general use of streamlit and langchain for rapid development/prototyping.

The results from OpenAI API + RAG:

Prompt: What is the best great league team in pokemon go?

Response: The best Great League team can vary based on the current meta, but a strong combination often includes:

Altaria (Dragon/Flying) 
– Great bulk and access to powerful moves like Sky Attack.
Galarian Stunfisk (Ground/Steel)
– Excellent typing and moveset with Mud Shot and Earthquake.
Deoxys (Defense Forme) (Psychic) 
– Great bulk and access to counter moves like Counter and Psycho Boost.
This trio covers many prevalent threats and provides good synergy. Always consider adjusting your team based on the current meta and your playstyle!

The results from TinyLlama:

Prompt: What is pokemon go?

Response: What is pokemon go? The 2019-2020 school year is underway and we are excited to see all of our students back in the classroom. We are also excited to welcome our new students and families to our school. We are looking forward to a great year and hope that you will join us in our efforts to provide a safe and nurturing environment for all of our students. We are excited to welcome our new students and families



