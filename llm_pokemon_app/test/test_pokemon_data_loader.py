import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd

# Add the src folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from llm_pokemon_app.src.data.pokemon_data_loader import PokemonDataLoader


class TestPokemonDataLoader(unittest.TestCase):

    # Test case 1: Successful loading of a valid CSV file
    @patch('pandas.read_csv')
    def test_load_csv_success(self, mock_read_csv):
        # Create a sample DataFrame
        sample_data = pd.DataFrame({
            'ID': [1, 2],
            'NAME': ['Bulbasaur', 'Ivysaur'],
            'TYPE_ONE': ['Grass', 'Grass'],
            'TYPE_TWO': ['Poison', 'Poison'],
            'FAST_MOVE': ['Vine Whip', 'Vine Whip'],
            'FAST_MOVE_POWER': [7, 7],
            'FAST_MOVE_TYPE': ['Grass', 'Grass'],
            'FAST_ENERGY_BOOST': [4, 4],
            'FAST_MOVE_DURATION': [0.6, 0.6],
            'CHARGE_MOVE': ['Sludge Bomb', 'Sludge Bomb'],
            'CHARGE_MOVE_POWER': [80, 80],
            'CHARGED_MOVE_TYPE': ['Poison', 'Poison'],
            'CHARGE_MOVE_ENERGY_COST': [50, 50],
            'CHARGE_MOVE_DURATION': [2.3, 2.3],
            'DAMAGE_WINDOW_START': [1.2, 1.2]
        })

        # Mock the pandas read_csv method to return this sample DataFrame
        mock_read_csv.return_value = sample_data

        # Instantiate the loader and test
        df = PokemonDataLoader.load_csv("fake_path.csv")

        # Assert the data is loaded successfully
        self.assertIsInstance(df, pd.DataFrame)  # Assert this is a DataFrame
        self.assertEqual(len(df), 2)  # We added 2 rows
        self.assertIn("NAME", df.columns)
        self.assertEqual(df.iloc[0]["NAME"], "Bulbasaur")

    # Test case 2: Handling invalid file path for CSV
    @patch('pandas.read_csv')
    def test_load_csv_invalid_path(self, mock_read_csv):
        # Mock read_csv to raise an error
        mock_read_csv.side_effect = FileNotFoundError("File not found")

        # Test the CSV loading with an invalid path
        result = PokemonDataLoader.load_csv("non_existing_file.csv")

        # Assert error message
        self.assertEqual(result, "File not found: File not found")

    # Test case 3: Empty file case for CSV
    @patch('pandas.read_csv')
    def test_load_csv_empty_file(self, mock_read_csv):
        # Mock read_csv to return an empty DataFrame
        mock_read_csv.return_value = pd.DataFrame()

        # Test the CSV loader with an empty file
        df = PokemonDataLoader.load_csv("empty_file.csv")

        # Assert empty DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)

    # Test case 4: Successful loading of a valid Excel file
    @patch('pandas.read_excel')
    def test_load_excel_success(self, mock_read_excel):
        # Mock a DataFrame for Excel loading
        sample_data = pd.DataFrame({
            'ID': [1, 2],
            'NAME': ['Charmander', 'Charmeleon']
        })

        mock_read_excel.return_value = sample_data

        # Test the Excel loading
        df = PokemonDataLoader.load_excel("fake_path.xlsx")

        # Assert the data is loaded successfully
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn("NAME", df.columns)
        self.assertEqual(df.iloc[0]["NAME"], "Charmander")

    # Test case 5: Successful loading of a valid Parquet file
    @patch('pandas.read_parquet')
    def test_load_parquet_success(self, mock_read_parquet):
        # Mock a DataFrame for Parquet loading
        sample_data = pd.DataFrame({
            'ID': [3, 4],
            'NAME': ['Squirtle', 'Wartortle']
        })

        mock_read_parquet.return_value = sample_data

        # Test the Parquet loading
        df = PokemonDataLoader.load_parquet("fake_path.parquet")

        # Assert the data is loaded successfully
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn("NAME", df.columns)
        self.assertEqual(df.iloc[0]["NAME"], "Squirtle")


if __name__ == '__main__':
    unittest.main()