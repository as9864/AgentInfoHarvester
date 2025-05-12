from setuptools import setup, find_packages

setup(
    name="infoharvester",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "requests",
        "openai",
        "langchain",
        "langchain-community",
        "langchain-openai",
        "faiss-cpu",
        "python-dotenv"
    ],
)