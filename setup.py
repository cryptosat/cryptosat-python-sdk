from setuptools import setup, find_packages

setup(
    name="cryptosat",
    version="0.0.1",
    url="https://github.com/cryptosat/cryptosat-python-sdk",
    author="Amir Benvenisti",
    author_email="amirbenvenisti@cryptosat.io",
    description="Python SDK for Cryptosat confidential computing services",
    packages=find_packages(),  
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
)