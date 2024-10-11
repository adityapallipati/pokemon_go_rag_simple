"""
This module provides a HuggingFace model class for generating responses
using a causal language model (TinyLlama) via the Hugging Face API.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM


class HuggingFaceModel:
    """
    A class to interact with the Hugging Face API and
    generate responses using a pre-trained causal
    language model (TinyLlama).
    """

    def __init__(self, api_key: str):
        """
        Initialize the Hugging Face model with the provided API key.

        Args:
            api_key (str): The Hugging Face API key.
        """
        self.api_key = api_key

        # Load the tokenizer and model for causal language modeling
        self.tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama_v1.1")
        self.model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama_v1.1")

    def get_response(self, prompt: str) -> str:
        """
        Get the response from the Hugging Face model for the given prompt.

        Args:
            prompt (str): The input prompt/question.

        Returns:
            str: The human-readable response from the Hugging Face model.
        """
        try:
            # Tokenize the input prompt
            inputs = self.tokenizer(prompt, return_tensors="pt")

            # Generate text using the model,
            # setting pad_token_id to eos_token_id for open-end generation
            outputs = self.model.generate(
                **inputs,
                max_length=100,
                pad_token_id=self.tokenizer.eos_token_id,
            )

            # Decode the generated tokens into a human-readable response
            response_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            return response_text.strip()

        except (ValueError, RuntimeError) as error:
            return f"Error: {str(error)}"
