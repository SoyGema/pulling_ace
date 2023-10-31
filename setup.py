from setuptools import find_packages, setup

setup(
    name="pulling_ace",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "accelerate>=0.12.0",
        "datasets>=1.8.0",
        "sentencepiece!=0.1.92",
        "protobuf",
        "sacrebleu>=1.4.12",
        "torch>=1.3",
        "evaluate",
        "transformers",
        "safetensors",
        "wandb",
        "textattack",
        "beyond_the_nest>=1.18.0",
    ],
    entry_points={
        "console_scripts": [
            "pullingace = pulling_ace.cli:main",
        ],
    },
    "trunk>=1.18.0",
    "console_scripts": [
        "pullingace = pulling_ace.cli:main",
    ],
)
    "pullingace = pulling_ace.cli:main",

setup(
    name="pulling_ace",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "accelerate>=0.12.0",
        "datasets>=1.8.0",
        "sentencepiece!=0.1.92",
        "protobuf",
        "sacrebleu>=1.4.12",
        "torch>=1.3",
        "evaluate",
        "transformers",
        "safetensors",
        "wandb",
        "textattack",
        "beyond_the_nest>=1.18.0",
    ],
    entry_points={
        "console_scripts": [
            "beyond_the_nest = pulling_ace.cli:main",
        ],
    },
    "trunk>=1.18.0",
    "console_scripts": [
        "pullingace = pulling_ace.cli:main",
    ],
)
