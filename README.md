# Python SDK for Cryptosat Services

Cryptosat SDK provides a seamless way to integrate with Cryptosat services directly from your Python application.

## Installation

    pip install cryptosat_python_sdk

## Local installation

    poetry install
    poetray shell

## Quick Start

```python
# Import Cryptosat client
from cryptosat.client import CryptosatClient

# Create a Cryptosat instance with the service URL
cryptosat = CryptosatClient('https://sandbox.api.cryptosat.io/v0')

# Fetch the version
version = cryptosat.version()
```

### Timestamp

```python
# Fetch the satellite timestamp
result = cryptosat.get_timestamp()
```

### Public randomness

```python
# Fetch public randomness from the Cryptosat
randomness = cryptosat.get_public_random()
```

### Message signing

```python
# Initiate the signing request
sign_request = cryptosat.sign_message("Hello, world!")

# Poll the status of the request until it is ready
status = sign_request.get_status()
while status != RequestStatus.READY:
    print(status)
    time.sleep(5)
    status = sign_request.get_status()

# Once ready, retrieve the result
result = sign_request.result
```

### Ballot

```python

```

### Delay Encryption

```python

```
