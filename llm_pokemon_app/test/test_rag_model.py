import unittest
from unittest.mock import patch, MagicMock
from llm_pokemon_app.src.models.rag_model import RAGModel
from llm_pokemon_app.src.utils.langchain_helpers import PokemonRetriever


class TestRAGModel(unittest.TestCase):

    @patch('llm_pokemon_app.src.models.rag_model.OpenAI')
    def test_get_response_success(self, mock_openai):
        # Mock the retriever
        mock_retriever = MagicMock()
        mock_retriever.retrieve_highest_dps.return_value = {
            'NAME': 'Mewtwo',
            'TOTAL_DPS': 30.5
        }

        # Mock OpenAI completion response
        mock_openai_instance = MagicMock()
        mock_openai.return_value = mock_openai_instance
        mock_openai_instance.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Mewtwo is the strongest Pokémon."))]
        )

        # Instantiate the RAGModel with the mocked retriever and OpenAI client
        model = RAGModel(api_key="fake_api_key", retriever=mock_retriever)

        # Test the model with a sample prompt
        response = model.get_response("What is the highest DPS Pokémon?")

        # Assert that the response is correct
        self.assertEqual(response, "Mewtwo is the strongest Pokémon.")

    @patch('llm_pokemon_app.src.models.rag_model.OpenAI')
    def test_retrieve_moves_success(self, mock_openai):
        # Mock the retriever
        mock_retriever = MagicMock()
        mock_retriever.retrieve_by_name.return_value = MagicMock(
            empty=False,
            iloc=[{
                'NAME': 'Charizard',
                'FAST_MOVE': 'Fire Spin',
                'FAST_MOVE_POWER': 10,
                'FAST_MOVE_TYPE': 'Fire',
                'CHARGE_MOVE': 'Blast Burn',
                'CHARGE_MOVE_POWER': 110,
                'CHARGED_MOVE_TYPE': 'Fire'
            }]
        )

        # Mock OpenAI completion response
        mock_openai_instance = MagicMock()
        mock_openai.return_value = mock_openai_instance
        mock_openai_instance.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Charizard has powerful fire-type moves."))]
        )

        # Instantiate the RAGModel with the mocked retriever and OpenAI client
        model = RAGModel(api_key="fake_api_key", retriever=mock_retriever)

        # Test the model with a sample prompt
        response = model.get_response("What are Charizard's moves?")

        # Assert that the response is correct
        self.assertEqual(response, "Charizard has powerful fire-type moves.")



if __name__ == '__main__':
    unittest.main()