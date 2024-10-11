import unittest
from unittest.mock import patch
import pandas as pd
from llm_pokemon_app.src.data.pokemon_data_loader import PokemonDataLoader


class TestPokemonDataLoader(unittest.TestCase):

    # Test case 1: Successful loading of a valid CSV file
    @patch('pandas.read_csv')
    def test_load_csv_success(self, mock_read_csv):
        # Create a sample DataFrame
        sample_data = pd.DataFrame({
            'ID': [1, 2],
            'NAME': ['Bulbasaur', 'Ivysaur']
        })

        mock_read_csv.return_value = sample_data
        result = PokemonDataLoader.load_csv("valid_file.csv")

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]["NAME"], "Bulbasaur")

    # Test case 2: CSV File Not Found Error
    @patch('pandas.read_csv')
    def test_load_csv_file_not_found(self, mock_read_csv):
        mock_read_csv.side_effect = FileNotFoundError("File not found")
        result = PokemonDataLoader.load_csv("invalid_file.csv")

        self.assertEqual(result, "File not found: File not found")

    # Test case 3: CSV Empty Data Error
    @patch('pandas.read_csv')
    def test_load_csv_empty_data_error(self, mock_read_csv):
        mock_read_csv.side_effect = pd.errors.EmptyDataError("Empty file")
        result = PokemonDataLoader.load_csv("empty_file.csv")

        self.assertEqual(result, "Empty data error: Empty file")

    # Test case 4: Successful loading of a valid Excel file
    @patch('pandas.read_excel')
    def test_load_excel_success(self, mock_read_excel):
        # Mock a DataFrame for Excel loading
        sample_data = pd.DataFrame({
            'ID': [1, 2],
            'NAME': ['Charmander', 'Charmeleon']
        })

        mock_read_excel.return_value = sample_data
        result = PokemonDataLoader.load_excel("valid_file.xlsx")

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]["NAME"], "Charmander")

    # Test case 5: Excel File Not Found Error
    @patch('pandas.read_excel')
    def test_load_excel_file_not_found(self, mock_read_excel):
        mock_read_excel.side_effect = FileNotFoundError("File not found")
        result = PokemonDataLoader.load_excel("invalid_file.xlsx")

        self.assertEqual(result, "File not found: File not found")

    # Test case 6: Excel Value Error
    @patch('pandas.read_excel')
    def test_load_excel_value_error(self, mock_read_excel):
        mock_read_excel.side_effect = ValueError("Value error")
        result = PokemonDataLoader.load_excel("invalid_file.xlsx")

        self.assertEqual(result, "Value error: Value error")

    # Test case 7: Successful loading of a valid Parquet file
    @patch('pandas.read_parquet')
    def test_load_parquet_success(self, mock_read_parquet):
        # Mock a DataFrame for Parquet loading
        sample_data = pd.DataFrame({
            'ID': [3, 4],
            'NAME': ['Squirtle', 'Wartortle']
        })

        mock_read_parquet.return_value = sample_data
        result = PokemonDataLoader.load_parquet("valid_file.parquet")

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]["NAME"], "Squirtle")

    # Test case 8: Parquet File Not Found Error
    @patch('pandas.read_parquet')
    def test_load_parquet_file_not_found(self, mock_read_parquet):
        mock_read_parquet.side_effect = FileNotFoundError("File not found")
        result = PokemonDataLoader.load_parquet("invalid_file.parquet")

        self.assertEqual(result, "File not found: File not found")

    # Test case 9: Parquet OS Error
    @patch('pandas.read_parquet')
    def test_load_parquet_os_error(self, mock_read_parquet):
        mock_read_parquet.side_effect = OSError("OS error")
        result = PokemonDataLoader.load_parquet("invalid_file.parquet")

        self.assertEqual(result, "OS error: OS error")


if __name__ == '__main__':
    unittest.main()