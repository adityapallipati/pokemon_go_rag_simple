"""
This module provides a RAG (Retrieval-Augmented Generation) model
that combines Pokémon Go data retrieval with OpenAI API response generation.
"""

from openai import OpenAI

from llm_pokemon_app.src.utils.langchain_helpers import PokemonRetriever  # type: ignore # pylint: disable=import-error


class RAGModel:
    """
    A class to interact with both a retriever for Pokémon Go data
    and the OpenAI API for generating responses.
    """

    def __init__(self, api_key: str, retriever: "PokemonRetriever"):
        """
        Initialize the RAG model with OpenAI API and Pokémon Go retriever.

        Args:
            api_key (str): OpenAI API key for GPT models.
            retriever (PokemonRetriever): A retriever object to retrieve Pokémon data.
        """
        self.client = OpenAI(api_key=api_key)
        self.retriever = retriever

    def retrieve_context(self, query: str) -> str:
        """
        Retrieve relevant Pokémon data from the dataset based on the query.

        Args:
            query (str): The user input question.

        Returns:
            str: A context string with relevant information from the Pokémon Go dataset.
        """
        if "highest dps" in query.lower():
            highest_dps_pokemon = self.retriever.retrieve_highest_dps()
            return (
                f"The Pokémon with the highest DPS is {highest_dps_pokemon['NAME']} "
                f"with a DPS of {highest_dps_pokemon['TOTAL_DPS']}."
            )

        if "moves" in query.lower():
            pokemon_name = query.split()[-1]
            moves = self.retriever.retrieve_by_name(pokemon_name)
            if not moves.empty:
                moves_info = moves.iloc[0]
                return (
                    f"{moves_info['NAME']}'s moves: {moves_info['FAST_MOVE']} "
                    f"(Fast, Power: {moves_info['FAST_MOVE_POWER']}, "
                    f"Type: {moves_info['FAST_MOVE_TYPE']}), "
                    f"{moves_info['CHARGE_MOVE']} "
                    f"(Charge, Power: {moves_info['CHARGE_MOVE_POWER']}, "
                    f"Type: {moves_info['CHARGED_MOVE_TYPE']})."
                )
            return "Sorry, I couldn't find the moves for that Pokémon."

        return "Sorry, I couldn't find any relevant data."

    def get_response(self, prompt: str) -> str:
        """
        Get the response from the RAG model by combining retrieval and OpenAI API generation.

        Args:
            prompt (str): The input prompt/question.

        Returns:
            str: The generated response augmented with retrieved data.
        """
        try:
            # Step 1: Retrieve context from the Pokémon dataset
            context = self.retrieve_context(prompt)

            # Step 2: Use OpenAI API to generate a response with the context
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant with expert knowledge of Pokémon Go. "
                            f"Keep your response to 150 tokens only. Additional context: {context}."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=150,
                temperature=0.7,
            )

            return response.choices[0].message.content

        except (ValueError, RuntimeError) as error:
            return f"Error: {str(error)}"
