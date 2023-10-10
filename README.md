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

## Usage

### Satellite metrics

```python
# Fetch the satellite timestamp
result = cryptosat.get_timestamp()

# Fetch the version
version = cryptosat.version()

# Fetch the satellite signing key
public_key = cryptosat.get_public_signing_key()

# If the cryptosat is offline you can query for the next time it will be online
next_online = cryptosat.get_next_online()
```

### Validate Signature

```python
from cryptosat.client import CryptosatClient
from cryptosat.binary import pem2bytes, int2bytes
import nacl.signing
import nacl.encoding

cryptosat = CryptosatClient('https://sandbox.api.cryptosat.io/v0')

result = cryptosat.get_timestamp()

# Convert timestamp and its signature to bytes
timestamp_bytes = int2bytes(result.timestamp)
signature_bytes = bytes.fromhex(result.signature)

# Fetch the public signing key from the Cryptosat
signing_key = cryptosat.get_public_signing_key()

# Convert signing key to bytes
signing_key_bytes = pem2bytes(signing_key)

# Verify signature
verify_key = nacl.signing.VerifyKey(signing_key_bytes)
verify_key.verify(timestamp_bytes, signature_bytes)
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
# Initiate the keypair
keypair = cryptosat.create_keypair(delay="60s")

# Poll the public key of the keypair creation until it is ready
public_key = keypair.try_fetch_public_key()
while public_key is None:
    time.sleep(5)
    public_key = keypair.try_fetch_public_key()

# Wait until private key is released
time.sleep(60)
    
# Poll the private key  until it is ready
private_key = keypair.try_fetch_private_key()
while private_key is None:
    time.sleep(5)
    private_key = keypair.try_fetch_private_key()
```
