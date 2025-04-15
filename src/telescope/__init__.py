"""
Telescope: A unified client for LLM models.

Sample: 

from telescope import get_client
client = get_client(vendor='anthropic')

"""
from .llm_client_interface import get_client

__all__ = ['get_client']
