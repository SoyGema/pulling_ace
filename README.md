# PullingAce: Benchmarking Robustness for LLM Models

> [!NOTE]
> Repository under active construction

PullingAce is a Python library designed to benchmark adversarial attacks on Hugging Face models. Built on top of TextAttack, PullingAce incorporates a set of recipes to assess the robustness of various natural language processing models. This tool provides a comprehensive evaluation of model vulnerabilities and helps researchers and practitioners in the field of machine learning understand the strengths and weaknesses of different models.

## Features for Classification

- **Adversarial Attack Benchmarks**: PullingAce provides a collection of adversarial attack benchmarks tailored for Hugging Face models. Evaluate model robustness against state-of-the-art attacks.

- **Incorporating TextAttack Recipes**: PullingAce integrates TextAttack's powerful attack recipes, making it easy to experiment with different attack strategies and customize evaluations.

- **Effortless Evaluation**: With PullingAce, you can effortlessly assess the performance of your Hugging Face models against adversarial attacks. Obtain detailed insights into your model's strengths and areas for improvement.

## Features for Generative Models


## Installation

To get started with PullingAce, you can install it using pip:

```bash
pip install pullingace

## Try
pullingace --attack tomato --model "textattack/albert-base-v2-ag-news" --dataset "ag_news" --num-examples 5

```

## Credits
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
## pulling_ace/utils/subprocessor.py

The `pulling_ace/utils/subprocessor.py` script is a Python script that contains several functions related to toxicity and prompt injection. These functions are used to run the Garak tool with different probes and evaluate the robustness of natural language processing models.

### Functions

#### toxicity

The `toxicity` function runs the Garak tool with probes from the 'realtoxicityprompts' family. It takes three parameters: `model_type` (the type of the model), `model_name` (the name of the model), and `probe` (the probe to be used). It validates that the probe belongs to the 'realtoxicityprompts' family and then executes the Garak tool with the specified parameters.

#### promptinjection

The `promptinjection` function runs the Garak tool with prompt injection using specified probes from the 'promptinject' family. It takes the same parameters as the `toxicity` function and performs similar validation and execution steps.

#### promptinjection_wrapper

The `promptinjection_wrapper` function is a wrapper function that is used to pass the parameters to the `promptinjection` function.

#### toxicity_wrapper

The `toxicity_wrapper` function is a wrapper function that is used to pass the parameters to the `toxicity` function.

#### run_injections

The `run_injections` function is the main function that runs the probes based on the specified probe family. It takes three parameters: `model_type`, `model_name`, and `probe_family`. It uses multiprocessing to parallelize the execution of the probes. If the probe family is 'promptinject', it creates a list of arguments for the `promptinjection_wrapper` function and maps them to the pool. If the probe family is 'realtoxicityprompts', it does the same for the `toxicity_wrapper` function. If an invalid probe family is selected, it prints an error message.

### Example Usage

To use the `run_injections` function with the `promptinject` probe family, you can call it as follows:

```python
run_injections("huggingface", "gpt2", "promptinject")
```
=======
## pulling_ace/utils/subprocessor.py

The `pulling_ace/utils/subprocessor.py` script is a Python script that contains several functions related to toxicity and prompt injection. These functions are used to run the Garak tool with different probes and evaluate the robustness of natural language processing models.

### Functions

#### toxicity

The `toxicity` function runs the Garak tool with probes from the 'realtoxicityprompts' family. It takes three parameters: `model_type` (the type of the model), `model_name` (the name of the model), and `probe` (the probe to be used). It validates that the probe belongs to the 'realtoxicityprompts' family and then executes the Garak tool with the specified parameters.

#### promptinjection

The `promptinjection` function runs the Garak tool with prompt injection using specified probes from the 'promptinject' family. It takes the same parameters as the `toxicity` function and performs similar validation and execution steps.

#### promptinjection_wrapper

The `promptinjection_wrapper` function is a wrapper function that is used to pass the parameters to the `promptinjection` function.

#### toxicity_wrapper

The `toxicity_wrapper` function is a wrapper function that is used to pass the parameters to the `toxicity` function.

#### run_injections

The `run_injections` function is the main function that runs the probes based on the specified probe family. It takes three parameters: `model_type`, `model_name`, and `probe_family`. It uses multiprocessing to parallelize the execution of the probes. If the probe family is 'promptinject', it creates a list of arguments for the `promptinjection_wrapper` function and maps them to the pool. If the probe family is 'realtoxicityprompts', it does the same for the `toxicity_wrapper` function. If an invalid probe family is selected, it prints an error message.

### Example Usage

To use the `run_injections` function with the `promptinject` probe family, you can call it as follows:

```python
run_injections("huggingface", "gpt2", "promptinject")
```
You can toxicity and prompt injection in your Hugginface model using garak probes calling --toxicity or --promptinjection.
pipenv run pre-commit install -t pre-push