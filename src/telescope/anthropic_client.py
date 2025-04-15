import os
import time

from typing import Optional

import anthropic

from .llm_client_interface import LLMClient


class AnthropicLLMClient(LLMClient):
    """
    LLM Client wrapper for Anthropic's Claude models.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = 'claude-3-sonnet-20240229'):
        """
        Initialize the Anthropic LLM Client.
        
        :param api_key: Anthropic API key. If not provided, will use ANTHROPIC_API_KEY env var
        :param model: Anthropic model to use (default: claude-3-sonnet-20240229)
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("Anthropic API key must be provided either as argument or ANTHROPIC_API_KEY env var")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model

    def send_message(
            self, 
            prompt: str, 
            max_tokens: int = 8000,
            **kwargs
        ) -> str:
            """
            Send a message to the Sonnet LLM and return the response.
            
            Args:
                prompt (str): The message/prompt to send to the model
                max_tokens (int, optional): Maximum tokens to generate. Defaults to 8000.
                **kwargs: Additional parameters to pass to the API call
            
            Returns:
                str: The generated response from the model
            
            Raises:
                anthropic.APIError: If there's an issue with the API request
            """
            try:
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    **kwargs
                )
                
                return message.content[0].text
            
            except anthropic.RateLimitError as e:
                print("We reached to Rate Limit. Will retry request in a minutes")
                time.sleep(60)
                return  self.send_message(prompt, max_tokens, **kwargs)
            
            except Exception as e:
                print(f"Error in API request: {e}")
                raise
