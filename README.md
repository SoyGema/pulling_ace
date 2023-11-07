# PullingAce: Benchmarking Robustness for LLM Models

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

> [!NOTE]
> Repository under active construction

PullingAce is a Python library designed to benchmark adversarial attacks on Hugging Face models. Built on top of TextAttack and Garak, PullingAce incorporates a set of recipes and attacks to assess the robustness of various natural language processing models in classification and generation taks. This tool provides a comprehensive evaluation of model vulnerabilities and helps researchers and practitioners in the field of machine learning understand the strengths and weaknesses of different models.

## Features for Classification

- **Adversarial Attack Benchmarks**: PullingAce provides a collection of adversarial attack benchmarks tailored for Hugging Face models. Evaluate model robustness against state-of-the-art attacks.

- **Incorporating TextAttack Recipes**: PullingAce integrates TextAttack's powerful attack recipes, making it easy to experiment with different attack strategies and customize evaluations.

### CLI Example
This command runs the PullingAce tool with the 'tomato' attack on the 'textattack/albert-base-v2-ag-news' model using the 'ag_news' dataset and runs the attack on 5 examples.
```bash
pullingace --attack tomato --model "textattack/albert-base-v2-ag-news" --dataset "ag_news" --num-examples 5
```


Rebuild the Package: Navigate to the folder where your setup.py file is located and run the following command. This command rebuilds the PullingAce package.

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
# Install development dependencies. This includes all the packages required for development and testing.
pipenv install --dev
# Format the codebase using black before committing changes.
pipenv run black .
```

Check Installation: You can check if the package is installed correctly by running the following command. This command lists all installed Python packages and should include PullingAce if the installation was successful.

```bash
pip list
```

## Setup

- **Prompt Injection**: PullingAce integrates the prompt injection feature from the Garak library, allowing for more dynamic and flexible adversarial attacks.

- **Toxicity**: PullingAce incorporates Garak's toxicity features, providing additional metrics for evaluating model robustness.

### CLI Example
```bash
# This command runs the prompt injection feature of PullingAce on the 'amazon/MistralLite' model using the 'promptinject' probes.
pulling-ace-cli prompt_injection --model_type huggingface --model_name "amazon/MistralLite" --probes promptinject
```
Notes : the probes must fit the PROBE_FAMILIES name defined in subprocessor.

## Installation

To get started with PullingAce, follow these steps:

- Clone the repository: `git clone https://github.com/<username>/pullingace.git`
- Navigate to the root directory: `cd pullingace`
- Install the package using pip:

```bash
- Install the package using pip. This command installs the PullingAce package:

```bash
pip install pullingace
```

This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

HAPPY PATH 
```bash
# Install the project dependencies
pipenv install
# Install the PullingAce package
pip3 install .
# Install the Garak library, which is used for some features in PullingAce
pip3 install garak
```
Tested currently in main with pulling-ace-cli prompt_injection --model_type huggingface --model_name "amazon/MistralLite" --probes promptinject


```bash
pip uninstall pullingace
```
Replace  pullingace with the name of your package.

Increment the Version Number: If you've made changes that you want to distribute, it's a good practice to increment the version number in your setup.py file.

This is right now intented to be a python library 
Uninstall the Previous Version: If you have a previous version of the package installed, you can uninstall it first to avoid conflicts. You can use the following command for that:

HAPPY PATH 
```bash
pipenv install
pip3 install .
pip3 install garak (SEE WHY)
```
Tested currently in main with pulling-ace-cli prompt_injection --model_type huggingface --model_name "amazon/MistralLite" --probes promptinject


```bash
pip uninstall pullingace
```
Replace  pullingace with the name of your package.

Increment the Version Number: If you've made changes that you want to distribute, it's a good practice to increment the version number in your setup.py file. This ensures that the new version of your package is correctly identified.

```python
setup(
    name='your_package_name',
    version='0.2',  # Increment this number to reflect the new version of your package
    # ...
)
```
Clear Old Build Directories: Remove old build artifacts to make sure you're starting fresh. This ensures that your new build is not affected by any old build artifacts. Navigate to the folder containing setup.py and run:

```bash
# This command removes old build directories to ensure a fresh build
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
# Install development dependencies. This includes all the packages required for development and testing.
pipenv install --dev

# Setup pre-commit and pre-push hooks. These hooks run checks before commits and pushes to ensure code quality.
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```
