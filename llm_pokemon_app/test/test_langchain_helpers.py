import unittest
import pandas as pd
from llm_pokemon_app.src.utils.langchain_helpers import PokemonRetriever

class TestPokemonRetriever(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame to act as Pokémon dataset
        self.sample_data = pd.DataFrame({
            'NAME': ['Bulbasaur', 'Ivysaur', 'Charmander', 'Charizard'],
            'FAST_MOVE_POWER': [7, 8, 9, 10],
            'FAST_MOVE_DURATION': [1.0, 0.9, 0.8, 0.7],
            'CHARGE_MOVE_POWER': [50, 60, 70, 100],
            'CHARGE_MOVE_DURATION': [2.5, 2.4, 2.3, 2.0]
        })

        # Instantiate the PokemonRetriever with sample data
        self.retriever = PokemonRetriever(self.sample_data)

    def test_retrieve_by_name_success(self):
        # Test retrieving Pokémon by name
        result = self.retriever.retrieve_by_name('Charizard')

        # Assert that the result contains the right Pokémon
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['NAME'], 'Charizard')

    def test_retrieve_by_name_partial_match(self):
        # Test retrieving Pokémon by partial name
        result = self.retriever.retrieve_by_name('Char')

        # Assert that multiple rows are returned
        self.assertEqual(len(result), 2)
        self.assertIn('Charmander', result['NAME'].values)
        self.assertIn('Charizard', result['NAME'].values)

    def test_retrieve_by_name_case_insensitive(self):
        # Test case-insensitive retrieval
        result = self.retriever.retrieve_by_name('charizard')

        # Assert that the correct Pokémon is retrieved, regardless of case
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['NAME'], 'Charizard')

    def test_retrieve_highest_dps(self):
        # Test retrieving Pokémon with the highest DPS
        result = self.retriever.retrieve_highest_dps()

        # Calculate DPS manually for the expected result
        charizard_fast_dps = 10 / 0.7
        charizard_charge_dps = 100 / 2.0
        charizard_total_dps = charizard_fast_dps + charizard_charge_dps

        # Assert that Charizard has the highest DPS
        self.assertEqual(result['NAME'], 'Charizard')
        self.assertAlmostEqual(result['TOTAL_DPS'], charizard_total_dps)

    def test_retrieve_by_name_no_match(self):
        # Test when no Pokémon matches the name
        result = self.retriever.retrieve_by_name('Pikachu')

        # Assert that no rows are returned
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()