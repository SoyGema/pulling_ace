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