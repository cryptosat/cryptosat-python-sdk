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

# Poll the result of the request until it is ready
result = sign_request.try_fetch_result()
while result is None:
    time.sleep(5)
    result = sign_request.try_fetch_result()
```

### Ballot

```python
# Initiate the ballot
ballot = cryptosat.create_ballot(1)

# Poll the public key of the ballot creation until it is ready
public_key = ballot.try_fetch_public_key()
while public_key is None:
    time.sleep(5)
    public_key = ballot.try_fetch_public_key()

# Initiate vote request
ballot.vote("candidate-1")

# Initiate finalize ballot request
ballot.finalize()

# Poll the result of the ballot finalization until it is ready
result = ballot.try_fetch_result()
while result is None:
    time.sleep(5)
    result = ballot.try_fetch_result()
```

### Delay Encryption

```python

```
