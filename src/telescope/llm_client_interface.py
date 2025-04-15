from abc import ABC, abstractmethod
from typing import Optional


class LLMClient(ABC):
    """
    Abstract base class for Language Model Clients.
    Defines the interface for interacting with different LLM providers.
    """

    @abstractmethod
    def send_message(self, prompt: str, max_tokens: int = 1000, **kwargs) -> str:
        """
        Send a message to the LLM and return the response.
        
        Args:
            prompt (str): The message/prompt to send to the model
            max_tokens (int, optional): Maximum tokens to generate. Defaults to 1000.
            **kwargs: Additional parameters to pass to the API call
        
        Returns:
            str: The generated response from the model
        """
        pass


def get_client(vendor: str, model: Optional[str] = None, **kwargs):
    """
    Factory function to get an initialized LLM client.
    
    :param vendor: LLM vendor (currently 'anthropic' and 'gemini' are supported)
    :param model: Specific model to use (optional)
    :param kwargs: Additional initialization parameters
    :return: Initialized LLM client
    """
    # Import here to avoid circular imports
    from .anthropic_client import AnthropicLLMClient
    from .google_client import GoogleLLMClient

    vendor = vendor.lower()
    
    if vendor == 'anthropic':
        return AnthropicLLMClient(model=model or 'claude-3-sonnet-20240229', **kwargs)
    
    if vendor == 'google':
        return GoogleLLMClient(model=model or 'gemini-pro', **kwargs)
    
    raise ValueError(f"Unsupported LLM vendor: {vendor}")
