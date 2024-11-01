# pylint: disable=import-error, no-name-in-module
"""
This module provides a Streamlit-based app to interact with OpenAI, Hugging Face models,
and Pokémon Go data. Users can input questions about Pokémon Go, and
receive responses from the chosen model.
"""
import os
import sys
import streamlit as st # type: ignore

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from llm_pokemon_app.src.models.rag_model import RAGModel
from llm_pokemon_app.src.models.openai_model import OpenAIModel
from llm_pokemon_app.src.models.huggingface_model import HuggingFaceModel
from llm_pokemon_app.src.data.pokemon_data_loader import PokemonDataLoader
from llm_pokemon_app.src.utils.langchain_helpers import PokemonRetriever


class LLMApp:
    """
    A class that represents the Pokémon Go LLM App.
    This app lets users choose between OpenAI, Hugging Face,
    or RAG models to answer Pokémon Go-related questions.
    """

    def __init__(self):
        """Initialize the app with models and user-provided API keys."""
        self.openai_api_key = None
        self.huggingface_api_key = None
        self.model_choice = None
        self.retriever = None  # Initialize retriever as None

    @staticmethod
    def build_retriever():
        """
        Build and store the retriever (run once for RAG model).
        This method loads Pokémon Go data from a CSV and initializes the PokémonRetriever.
        """
        data_loader = PokemonDataLoader()
        pokemon_data = data_loader.load_csv(
            "src/excel_files/final_pokemon_dataset.csv"
        )  # Path to your CSV
        return PokemonRetriever(pokemon_data)

    def main(self):
        """Main method to run the Streamlit app."""
        st.title("Pokémon Go LLM App")

        # Secure input for API keys
        self.openai_api_key = st.text_input(
            "Enter your OpenAI API Key:", type="password"
        )
        self.huggingface_api_key = st.text_input(
            "Enter your Hugging Face API Key:", type="password"
        )

        # Select between models
        self.model_choice = st.selectbox(
            "Choose Model", ["OpenAI", "Hugging Face", "RAG with Pokémon Data"]
        )

        # Question input
        question = st.text_input("Ask a question about Pokémon Go:")

        # Handle model choices and run the respective model
        if st.button("Get Answer") and question:
            if self.model_choice == "OpenAI" and self.openai_api_key:
                model = OpenAIModel(self.openai_api_key)
                response = model.get_response(question)
            elif self.model_choice == "Hugging Face" and self.huggingface_api_key:
                model = HuggingFaceModel(self.huggingface_api_key)
                response = model.get_response(question)
            elif self.model_choice == "RAG with Pokémon Data" and self.openai_api_key:
                # Build the retriever once
                if self.retriever is None:
                    self.retriever = self.build_retriever()

                # Use RAG model with the retriever
                model = RAGModel(self.openai_api_key, self.retriever)
                response = model.get_response(question)
            else:
                response = "Please provide a valid API key and choose a model."

            st.write("Response:", response)


if __name__ == "__main__":
    app = LLMApp()
    app.main()
