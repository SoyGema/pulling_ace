import multiprocessing
import subprocess
import time

PROBE_FAMILIES = {
    "art": ["Tox"],
    "continuation": ["ContinueSlursReclaimedSlurs50"],
    "dan": [
        "Ablation_Dan_11_0",
        "AntiDAN",
        "ChatGPT_Developer_Mode_RANTI",
        "ChatGPT_Developer_Mode_v2",
        "ChatGPT_Image_Markdown",
        "DAN_Jailbreak",
        "DUDE",
        "Dan_10_0",
        "Dan_11_0",
        "Dan_6_0",
        "Dan_6_2",
        "Dan_7_0",
        "Dan_8_0",
        "Dan_9_0",
        "STAN",
    ],
    "encoding": [
        "InjectAscii85",
        "InjectBase16",
        "InjectBase2048",
        "InjectBase32",
        "InjectBase64",
        "InjectBraille",
        "InjectHex",
        "InjectMime",
        "InjectMorse",
        "InjectQP",
        "InjectROT13",
        "InjectUU",
    ],
    "glitch": ["Glitch", "Glitch100"],
    "goodside": ["Davidjl", "ThreatenJSON", "WhoIsRiley"],
    "knownbadsignatures": ["EICAR", "GTUBE", "GTphish"],
    "leakreplay": [
        "LiteratureCloze",
        "LiteratureCloze80",
        "LiteratureComplete",
        "LiteratureComplete80",
    ],
    "lmrc": [
        "Anthropomorphisation",
        "Bullying",
        "Deadnaming",
        "Profanity",
        "QuackMedicine",
        "SexualContent",
        "Sexualisation",
        "SlurUsage",
    ],
    "malwaregen": ["Evasion", "Payload", "SubFunctions", "TopLevel"],
    "misleading": ["FalseAssertion50"],
    "packagehallucination": ["Python"],
    "promptinject": [
        "HijackHateHumans",
        "HijackHateHumansMini",
        "HijackKillHumans",
        "HijackKillHumansMini",
        "HijackLongPrompt",
        "HijackLongPromptMini",
    ],
    "realtoxicityprompts": [
        "RTPBlank",
        "RTPFlirtation",
        "RTPIdentity_Attack",
        "RTPInsult",
        "RTPProfanity",
        "RTPSevere_Toxicity",
        "RTPSexually_Explicit",
        "RTPThreat",
    ],
    "snowball": [
        "GraphConnectivity",
        "GraphConnectivityMini",
        "Primes",
        "PrimesMini",
        "Senators",
        "SenatorsMini",
    ],
    "test": ["Blank"],
    "xss": ["MarkdownImageExfil"],
}


def toxicity(model_type, model_name, probe):
    """
    Run the Garak tool with probes from the 'realtoxicityprompts' family.

    Parameters:
    model_type (str): The type of the model (e.g., "huggingface").
    model_name (str): The name of the model (e.g., "gpt2").
    probe (str): The probe to be used (e.g., "RTPBlank").
    """
    print(f"Executing toxicity with model_type: {model_type}, model: {model_name}, probes: {probe}")

    # Validate that the probe belongs to the 'realtoxicityprompts' family
    if probe not in PROBE_FAMILIES.get("realtoxicityprompts", []):
        print(f"Invalid probe {probe} for 'realtoxicityprompts' family")
        return

    command = [
        "python3",
        "-m",
        "garak",
        "--model_type",
        model_type,
        "--model_name",
        model_name,
        "--probes",
        f"realtoxicityprompts.{probe}",
    ]

    try:
        completed_process = subprocess.run(
            command, check=True, capture_output=True, text=True
        )
        print("Return code:", completed_process.returncode)
        print("Standard Output:\n{}".format(completed_process.stdout))
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command. Error: {e}")


def promptinjection(model_type, model_name, probe):
    """
    Run the Garak tool with prompt injection using specified probes from the 'promptinject' family.

    Parameters:
    model_type (str): The type of the model (e.g., "huggingface").
    model_name (str): The name of the model (e.g., "gpt2").
    probe (str): The probe to be used (e.g., "HijackHateHumans").
    """
    # Validate that the probe belongs to the 'promptinject' family
    if probe not in PROBE_FAMILIES.get("promptinject", []):
        print(f"Invalid probe {probe} for 'promptinject' family")
        return

    command = [
        "python3",
        "-m",
        "garak",
        "--model_type",
        model_type,
        "--model_name",
        model_name,
        "--probes",
        f"promptinject.{probe}",
    ]

    try:
        completed_process = subprocess.run(
            command, check=True, capture_output=True, text=True
        )
        print("Return code:", completed_process.returncode)
        print("Standard Output:\n{}".format(completed_process.stdout))
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command. Error: {e}")


def riskcards(model_type, model_name, probe):
    """
    Run the Garak tool with LanguageModels RiskCards using specified probes from the 'lmrc' family.

    Parameters:
    model_type (str): The type of the model (e.g., "huggingface").
    model_name (str): The name of the model (e.g., "gpt2").
    probe (str): The probe to be used (e.g., "Bullying").
    """
    print(f"Executing riskcards with model_type: {model_type}, model: {model_name}, probes: {probe}")
    # Validate that the probe belongs to the 'promptinject' family
    if probe not in PROBE_FAMILIES.get("lmrc", []):
        print(f"Invalid probe {probe} for 'riskcard' family")
        return

    command = [
        "python3",
        "-m",
        "garak",
        "--model_type",
        model_type,
        "--model_name",
        model_name,
        "--probes",
        f"lmrc.{probe}",
    ]

    try:
        completed_process = subprocess.run(
            command, check=True, capture_output=True, text=True
        )
        print("Return code:", completed_process.returncode)
        print("Standard Output:\n{}".format(completed_process.stdout))
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command. Error: {e}")


def riskcard_wrapper(args):
    return riskcards(args["model_type"], args["model_name"], args["probe"])


def promptinjection_wrapper(args):
    return promptinjection(args["model_type"], args["model_name"], args["probe"])


def toxicity_wrapper(args):
    return toxicity(args["model_type"], args["model_name"], args["probe"])


def run_injections(model_type, model_name, probe_family):
    """
    Run the probes based on the specified probe family.

    Parameters:
    model_type (str): The type of the model (e.g., "huggingface").
    model_name (str): The name of the model (e.g., "gpt2").
    probe_family (str): The family of the probes to be run (e.g., "promptinject" or "realtoxicityprompts").
    """
    with multiprocessing.Pool(processes=2) as pool:
        if probe_family == "promptinject":
            args_list = [
                {
                    "model_type": model_type,
                    "model_name": model_name,
                    "probe": probe,
                }
                for probe in PROBE_FAMILIES.get("promptinject", [])
            ]
            start_time = time.time()

            print(f"Starting probe injections for {probe_family}")
            results = pool.map(promptinjection_wrapper, args_list)
            end_time = time.time()

            print(f"Completed probe injections for {probe_family}")
            print(f"Probe injection took {end_time - start_time} seconds.")



        elif probe_family == "realtoxicityprompts":
            args_list = [
                {
                    "model_type": model_type,
                    "model_name": model_name,
                    "probe": probe,
                }
                for probe in PROBE_FAMILIES.get("realtoxicityprompts", [])
            ]
            results = pool.map(toxicity_wrapper, args_list)
        elif probe_family == "lmrc":
            args_list = [
                {
                    "model_type": model_type,
                    "model_name": model_name,
                    "probe": probe,
                }
                for probe in PROBE_FAMILIES.get("lmrc", [])
            ]
            pool.map(toxicity_wrapper, args_list)
        else:
            print(f"Invalid probe family '{probe_family}' selected.")

