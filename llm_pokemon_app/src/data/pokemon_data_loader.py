"""
This module provides a class for loading Pokémon Go data from multiple file formats.
Supported formats include CSV, Excel, and Parquet, with appropriate error handling.
"""

import pandas as pd


class PokemonDataLoader:
    """
    A loader class that provides methods for loading Pokémon Go data from CSV, Excel,
    and Parquet files. It provides error handling for missing files and
    incorrect data formats.
    """

    @staticmethod
    def load_csv(file_path: str) -> pd.DataFrame:
        """
        Load Pokémon Go data from a CSV file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: Loaded Pokémon Go data as a pandas DataFrame.
        """
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError as error:
            return f"File not found: {str(error)}"
        except pd.errors.EmptyDataError as error:
            return f"Empty data error: {str(error)}"
        except pd.errors.ParserError as error:
            return f"Parser error: {str(error)}"
        except pd.errors.DtypeWarning as error:
            return f"Data type warning: {str(error)}"
        # Removed broad exception handling here.

    @staticmethod
    def load_excel(file_path: str) -> pd.DataFrame:
        """
        Load Pokémon Go data from an Excel file.

        Args:
            file_path (str): The path to the Excel file.

        Returns:
            pd.DataFrame: Loaded Pokémon Go data as a pandas DataFrame.
        """
        try:
            return pd.read_excel(file_path)
        except FileNotFoundError as error:
            return f"File not found: {str(error)}"
        except pd.errors.EmptyDataError as error:
            return f"Empty data error: {str(error)}"
        except ValueError as error:
            return f"Value error: {str(error)}"
        # Removed broad exception handling here.

    @staticmethod
    def load_parquet(file_path: str) -> pd.DataFrame:
        """
        Load Pokémon Go data from a Parquet file.

        Args:
            file_path (str): The path to the Parquet file.

        Returns:
            pd.DataFrame: Loaded Pokémon Go data as a pandas DataFrame.
        """
        try:
            return pd.read_parquet(file_path)
        except FileNotFoundError as error:
            return f"File not found: {str(error)}"
        except pd.errors.EmptyDataError as error:
            return f"Empty data error: {str(error)}"
        except OSError as error:
            return f"OS error: {str(error)}"
