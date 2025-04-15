# Telescope

Single entrypoint into LLM world

## Overview

Telescope provides a unified, simple interface for interacting with multiple Language Model (LLM) providers, making it easy to switch between different AI models with minimal code changes.

## Features

- Unified client interface
- Support for multiple LLM providers
- Simple configuration
- Minimal boilerplate code

## Quick Start

```python
from telescope import get_client

# Get an Anthropic client
anthropic_client = get_client('anthropic')

# Get a Google client
google_client = get_client('google')

# Send a message
response = anthropic_client.send_message("Write a short poem about AI")
```

## Supported Providers

- Anthropic
- Google Generative AI

## Installation

```bash
pip install telescope
```

## Requirements

- Python 3.8+
- typing_extensions==4.12.2
- anthropic==0.49.0
- google-genai==1.9.0

## License

MIT License

## Contact

Vitalii Kostenko
Digital Galaxy LLC
