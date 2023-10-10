from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def int2bytes(integer: int) -> bytes:
    return integer.to_bytes(8, byteorder="little")


def pem2bytes(pem: str) -> bytes:
    pem_encoded = pem.encode()
    loaded_public_key = serialization.load_pem_public_key(pem_encoded, backend=default_backend())

    return loaded_public_key.public_bytes(
        encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw
    )
