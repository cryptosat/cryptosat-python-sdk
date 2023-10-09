# Python SDK for Cryptosat Services

Cryptosat SDK provides a seamless way to integrate with Cryptosat services directly from your Python application.

## Installation

    pip install cryptosat_python_sdk

## Local installation

    poetry install
    poetray shell

## Quick Start

```python
from cryptosat.client import CryptosatClient

# Create a Cryptosat instance with the service URL
cryptosat = CryptosatClient('https://sandbox.api.cryptosat.io/v0')

# Fetch the version
version = cryptosat.version()
```
