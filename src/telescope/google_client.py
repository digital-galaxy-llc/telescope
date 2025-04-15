import os
from typing import Optional

from google import genai

from .llm_client_interface import LLMClient


class GoogleLLMClient(LLMClient):
    """
    LLM Client wrapper for Google's Gemini models.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = 'gemini-pro'):
        """
        Initialize the Google LLM Client.
        
        :param api_key: Google AI API key. If not provided, will use GOOGLE_API_KEY env var
        :param model: Google Gemini model to use (default: gemini-pro)
        """
        self.api_key = api_key or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("Google API key must be provided either as argument or GOOGLE_API_KEY env var")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def send_message(
            self, 
            prompt: str, 
            max_tokens: int = 1000,
            **kwargs
        ) -> str:
            """
            Send a message to the Gemini LLM and return the response.
            
            Args:
                prompt (str): The message/prompt to send to the model
                max_tokens (int, optional): Maximum tokens to generate. Defaults to 1000.
                **kwargs: Additional parameters to pass to the API call
            
            Returns:
                str: The generated response from the model
            
            Raises:
                Exception: If there's an issue with the API request
            """
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                return response.text
            
            except Exception as e:
                print(f"Error in API request: {e}")
                raise
