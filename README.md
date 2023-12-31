# PullingAce: Benchmarking Robustness for LLM Models

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

> [!NOTE]
> Repository under active construction

<img width="764" alt="Captura de pantalla 2024-01-08 a las 15 07 17" src="https://github.com/SoyGema/pulling_ace/assets/24204714/77f7bdab-edb8-4925-8ca8-45b8743cb21a">


https://github.com/SoyGema/pulling_ace/assets/24204714/9c1edbf6-2949-43c6-805e-c9d6995d78aa


PullingAce is a Python library designed to benchmark adversarial attacks on Hugging Face models. Built on top of TextAttack and Garak, PullingAce incorporates a set of recipes and attacks to assess the robustness of various natural language processing models in classification and generation taks. This tool provides a comprehensive evaluation of model vulnerabilities and helps researchers and practitioners in the field of machine learning understand the strengths and weaknesses of different models.

## Features for Classification

- **Adversarial Attack Benchmarks**: PullingAce provides a collection of adversarial attack benchmarks tailored for Hugging Face models. Evaluate model robustness against state-of-the-art attacks.

- **Incorporating TextAttack Recipes**: PullingAce integrates TextAttack's powerful attack recipes, making it easy to experiment with different attack strategies and customize evaluations.

### CLI Example
```bash
pullingace --attack tomato --model "textattack/albert-base-v2-ag-news" --dataset "ag_news" --num-examples 10
```


## Features for Generative Models

- **Prompt Injection**: PullingAce integrates the prompt injection feature from the Garak library, allowing for more dynamic and flexible adversarial attacks.

- **Toxicity**: PullingAce incorporates Garak's toxicity features, providing additional metrics for evaluating model robustness.

- **Risk Cards**: This framework gives a large set of risks that might present in
LM deployment. Risks can affect a variety of actors in a variety
of ways. The set of risks is large, but not all risks apply in
all scenarios - and so not all lmrc probes will be relevant to 
every system.

- **Leak Replay** : Integrates probes for evaluating if a model will replay training data.

## Reports 

Creates an html report that analyzes the attack

### CLI Example
```bash
# Replace with a specific command for prompt injection
pullingace prompt_injection --model_type huggingface --model_name "amazon/MistralLite" --probes HijackHateHumans
```
Notes : the probes must fit the PROBE_FAMILIES name defined in subprocessor.

## Installation

To get started with PullingAce, follow these steps:

- Create virtual environment
- Clone the repository: `git clone https://github.com/<username>/pullingace.git`
- Navigate to the root directory: `cd pullingace`
- Install the package using pip:

```bash
pip install .

## Try
pullingace --attack tomato --model "textattack/albert-base-v2-ag-news" --dataset "ag_news" --num-examples 5

```

This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.



### Notes for Builds

This is right now intented to be a python library 
Uninstall the Previous Version: If you have a previous version of the package installed, you can uninstall it first to avoid conflicts. You can use the following command for that:

HAPPY PATH 
```bash
pipenv install
pip3 install .
pip3 install garak (SEE WHY)
```
Tested currently in main with pullingace prompt_injection --model_type huggingface --model_name "amazon/MistralLite" --probes promptinject


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
