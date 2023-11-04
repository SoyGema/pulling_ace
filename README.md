# PullingAce: Benchmarking Robustness for LLM Models

> [!NOTE]
> Repository under active construction

PullingAce is a Python library designed to benchmark adversarial attacks on Hugging Face models. Built on top of TextAttack and Garak, PullingAce incorporates a set of recipes to assess the robustness of various natural language processing models in classification and generation taks. This tool provides a comprehensive evaluation of model vulnerabilities and helps researchers and practitioners in the field of machine learning understand the strengths and weaknesses of different models.

## Features for Classification

- **Adversarial Attack Benchmarks**: PullingAce provides a collection of adversarial attack benchmarks tailored for Hugging Face models. Evaluate model robustness against state-of-the-art attacks.

- **Incorporating TextAttack Recipes**: PullingAce integrates TextAttack's powerful attack recipes, making it easy to experiment with different attack strategies and customize evaluations.

### CLI Example
```bash
pullingace --attack tomato --model "textattack/albert-base-v2-ag-news" --dataset "ag_news" --num-examples 5
```


## Features for Generative Models

- **Prompt Injection**: PullingAce integrates the prompt injection feature from the Garak library, allowing for more dynamic and flexible adversarial attacks.

- **Toxicity**: PullingAce incorporates Garak's toxicity features, providing additional metrics for evaluating model robustness.

### CLI Example
```bash
# Replace with a specific command for prompt injection
pullingace --attack promptinjection --model "textattack/albert-base-v2-ag-news" 
```

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
=======
# PullingAce: Benchmarking Robustness for LLM Models

## Installation

To get started with PullingAce, follow these steps:

- Clone the repository: `git clone https://github.com/<username>/pullingace.git`
- Navigate to the root directory: `cd pullingace`
- Install the package using pip:

```bash
pip install pullingace

## Try
pullingace --attack tomato --model "textattack/albert-base-v2-ag-news" --dataset "ag_news" --num-examples 5

```

This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.



### Notes for Builds

This is right now intented to be a python library 
Uninstall the Previous Version: If you have a previous version of the package installed, you can uninstall it first to avoid conflicts. You can use the following command for that:

```bash
pip uninstall pullingace
```
Replace  pullingace with the name of your package.

Increment the Version Number: If you've made changes that you want to distribute, it's a good practice to increment the version number in your setup.py file.

```python
setup(
    name='your_package_name',
    version='0.2',  # Increment this number
    # ...
)
```
Clear Old Build Directories: Remove old build artifacts to make sure you're starting fresh. Navigate to the folder containing setup.py and run:

```bash
Copy code
rm -rf build dist pulling_ace.egg-info
```


Rebuild the Package: Navigate to the folder where your setup.py file is located and run:

```bash
pip install .
```

Check Installation: You can check if the package is installed correctly by running:

```bash
Copy code
pip list
```

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push