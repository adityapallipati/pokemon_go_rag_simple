import unittest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from llm_pokemon_app.src.app import LLMApp


class TestLLMApp(unittest.TestCase):

    @patch('llm_pokemon_app.src.app.st.write')
    @patch('llm_pokemon_app.src.app.st.button')
    @patch('llm_pokemon_app.src.app.st.selectbox')
    @patch('llm_pokemon_app.src.app.st.text_input')
    @patch('llm_pokemon_app.src.app.OpenAIModel')
    def test_openai_model_response(self, mock_openai_model, mock_text_input, mock_selectbox, mock_button, mock_write):
        # Simulate the text input for API key and question
        mock_text_input.side_effect = ["fake_openai_api_key", "", "What is the best Pokémon in Pokémon Go?"]
        mock_selectbox.return_value = "OpenAI"
        mock_button.return_value = True  # Simulate button press

        # Mock the OpenAI model's response
        mock_openai_instance = MagicMock()
        mock_openai_instance.get_response.return_value = "Mewtwo is the best Pokémon."
        mock_openai_model.return_value = mock_openai_instance  # Ensure the instance returns the mock

        # Instantiate the src.app and run the main method
        app = LLMApp()
        app.main()

        # Assert st.write was called with expected values
        mock_write.assert_called_with("Response:", "Mewtwo is the best Pokémon.")

    @patch('llm_pokemon_app.src.app.st.write')
    @patch('llm_pokemon_app.src.app.st.button')
    @patch('llm_pokemon_app.src.app.st.selectbox')
    @patch('llm_pokemon_app.src.app.st.text_input')
    @patch('llm_pokemon_app.src.app.HuggingFaceModel')
    def test_huggingface_model_response(self, mock_huggingface_model, mock_text_input, mock_selectbox, mock_button, mock_write):
        # Simulate the text input for API key and question
        mock_text_input.side_effect = ["", "fake_huggingface_api_key", "What are Charizard's moves?"]
        mock_selectbox.return_value = "Hugging Face"
        mock_button.return_value = True  # Simulate button press

        # Mock the Hugging Face model's response
        mock_huggingface_instance = MagicMock()
        mock_huggingface_instance.get_response.return_value = "Charizard has Fire Spin and Blast Burn."
        mock_huggingface_model.return_value = mock_huggingface_instance

        # Instantiate the src.app and run the main method
        app = LLMApp()
        app.main()

        # Assert st.write was called with expected values
        mock_write.assert_called_with("Response:", "Charizard has Fire Spin and Blast Burn.")

    @patch('llm_pokemon_app.src.app.st.write')
    @patch('llm_pokemon_app.src.app.st.button')
    @patch('llm_pokemon_app.src.app.st.selectbox')
    @patch('llm_pokemon_app.src.app.st.text_input')
    @patch('llm_pokemon_app.src.app.RAGModel')
    def test_rag_model_response(self, mock_rag_model, mock_text_input, mock_selectbox, mock_button, mock_write):
        # Simulate the text input for API key and question
        mock_text_input.side_effect = ["fake_openai_api_key", "", "What is the highest DPS Pokémon?"]
        mock_selectbox.return_value = "RAG with Pokémon Data"
        mock_button.return_value = True  # Simulate button press

        # Mock the RAG model's response
        mock_rag_instance = MagicMock()
        mock_rag_instance.get_response.return_value = "Mewtwo has the highest DPS."
        mock_rag_model.return_value = mock_rag_instance

        # Instantiate the src.app and run the main method 
        app = LLMApp()
        app.main()

        # Assert st.write was called with expected values
        mock_write.assert_called_with("Response:", "Mewtwo has the highest DPS.")


if __name__ == '__main__':
    unittest.main()