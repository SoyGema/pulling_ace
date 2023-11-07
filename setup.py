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
    ],
    # The entry_points dictionary specifies the console scripts that should be created when the package is installed.
    # The console_scripts entry has been updated to include the main function of the pulling_ace.cli module as a console script.
    entry_points={
        "console_scripts": [
            "pullingace = pulling_ace.cli:main",  # This command will run the main function from the pulling_ace.cli module
        ],
    },
    # The install_requires list specifies the dependencies that need to be installed for this package.
    # The dependencies have been updated to include new packages that are required for the latest features of the pulling_ace package.
    install_requires=[
        "accelerate>=0.12.0",  # Used for accelerating Python programs with GPUs
        "datasets>=1.8.0",  # Provides a collection of datasets ready to use with PyTorch, TensorFlow, etc.
        "sentencepiece!=0.1.92",  # A language-independent subword tokenizer preprocessor
        "protobuf",  # Google's data interchange format
        "sacrebleu>=1.4.12",  # A standard BLEU score implementation
        "torch>=1.3",  # PyTorch, a deep learning platform
        "evaluate",  # A package for evaluation metrics
        "transformers",  # Provides state-of-the-art general-purpose architectures for Natural Language Understanding (NLU) and Natural Language Generation (NLG)
        "safetensors",  # A package for safe tensor operations
        "wandb",  # A tool for visualizing and tracking machine learning experiments
        "textattack",  # A Python framework for adversarial attacks, data augmentation, and model training in NLP
    ],
    entry_points={
        "console_scripts": [
            "pullingace = pulling_ace.cli:main",
        ],
    },
)
