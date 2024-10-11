"""
This module provides an interface to interact with OpenAI's GPT models via an API.
It uses the OpenAI API to send prompts and retrieve responses from the GPT models.
"""

from openai import OpenAI  # type: ignore # pylint: disable=import-error


class OpenAIModel:
    """
    A class to interact with OpenAI's GPT models using the provided API key.
    """

    def __init__(self, api_key: str):
        """
        Initialize the OpenAI model with the provided API key.

        Args:
            api_key (str): The OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)

    def get_response(self, prompt: str) -> str:
        """
        Get the response from OpenAI GPT-3 model for the given prompt.

        Args:
            prompt (str): The input prompt/question.

        Returns:
            str: The response from OpenAI.
        """
        try:
            # Sending a request to the GPT-4 model
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant with expert knowledge of Pokémon Go. "
                            "Keep your response to 150 tokens only."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=150
            )
            # Extracting the assistant's response content
            message_content = response.choices[0].message.content

            return message_content
        except (ValueError, TypeError) as error:
            return f"Error: {str(error)}"
