import unittest
from unittest.mock import patch, MagicMock
from llm_pokemon_app.src.models.openai_model import OpenAIModel

class TestOpenAIModel(unittest.TestCase):

    @patch('llm_pokemon_app.src.models.openai_model.OpenAI')
    def test_get_response_success(self, mock_openai):
        # Mock OpenAI completion response
        mock_openai_instance = MagicMock()
        mock_openai.return_value = mock_openai_instance
        mock_openai_instance.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="This is a Pokémon Go response."))]
        )

        # Instantiate the OpenAIModel with a fake API key
        model = OpenAIModel(api_key="fake_api_key")

        # Test the model with a sample prompt
        response = model.get_response("What is the best Pokémon in Pokémon Go?")

        # Assert that the response is correct
        self.assertEqual(response, "This is a Pokémon Go response.")


if __name__ == '__main__':
    unittest.main()