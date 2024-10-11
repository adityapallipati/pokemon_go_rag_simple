"""
This module provides a class for retrieving Pokémon Go data from a dataset.
It supports retrieving Pokémon by name and calculating the highest DPS (damage per second).
"""

import pandas as pd


class PokemonRetriever:
    """
    A class to retrieve Pokémon data from a dataset.

    This class allows for retrieving Pokémon by name and determining the Pokémon
    with the highest DPS (Damage Per Second).
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the Pokémon retriever with the provided dataset.

        Args:
            data (pd.DataFrame): Pokémon dataset as a pandas DataFrame.
        """
        self.data = data

    def retrieve_by_name(self, pokemon_name: str) -> pd.DataFrame:
        """
        Retrieve Pokémon data based on the Pokémon's name.

        Args:
            pokemon_name (str): Name of the Pokémon.

        Returns:
            pd.DataFrame: A filtered DataFrame with matching Pokémon rows.
        """
        return self.data[
            self.data["NAME"].str.contains(pokemon_name, case=False, na=False)
        ]

    def retrieve_highest_dps(self) -> pd.Series:
        """
        Retrieve the Pokémon with the highest DPS (calculated as Power / Duration
        for fast and charge moves).

        Returns:
            pd.Series: The row of the Pokémon with the highest DPS.
        """
        # Calculate DPS for each Pokémon (Fast DPS + Charge DPS)
        self.data["FAST_DPS"] = (
            self.data["FAST_MOVE_POWER"] / self.data["FAST_MOVE_DURATION"]
        )
        self.data["CHARGE_DPS"] = (
            self.data["CHARGE_MOVE_POWER"] / self.data["CHARGE_MOVE_DURATION"]
        )
        self.data["TOTAL_DPS"] = self.data["FAST_DPS"] + self.data["CHARGE_DPS"]

        # Find the Pokémon with the highest total DPS
        return self.data.loc[self.data["TOTAL_DPS"].idxmax()]
