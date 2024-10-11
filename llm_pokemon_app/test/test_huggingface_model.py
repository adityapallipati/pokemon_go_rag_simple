import unittest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from llm_pokemon_app.src.models.huggingface_model import HuggingFaceModel

class TestHuggingFaceModel(unittest.TestCase):

    @patch('llm_pokemon_app.src.models.huggingface_model.AutoTokenizer.from_pretrained')
    @patch('llm_pokemon_app.src.models.huggingface_model.AutoModelForCausalLM.from_pretrained')
    def test_get_response_success(self, mock_model, mock_tokenizer):
        # Create a mock tokenizer that simulates tokenizing a prompt
        mock_tokenizer_instance = MagicMock()
        mock_tokenizer_instance.return_tensors = "pt"
        mock_tokenizer.return_value = mock_tokenizer_instance

        # Create a mock model that simulates text generation
        mock_model_instance = MagicMock()
        mock_model_instance.generate.return_value = [[101, 202, 303]]  # Simulating token generation
        mock_model.return_value = mock_model_instance

        # Mock tokenizer decoding to simulate a human-readable response
        mock_tokenizer_instance.decode.return_value = "Hello, this is a generated response."

        # Instantiate the HuggingFaceModel
        model = HuggingFaceModel(api_key="fake_api_key")

        # Test with a sample prompt
        response = model.get_response("What is the best Pokémon?")

        # Assert that the response is as expected
        self.assertEqual(response, "Hello, this is a generated response.")

if __name__ == '__main__':
    unittest.main()