import subprocess

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


def promptinjection(model_type, model_name, probe_family, probe):
    """
    Run the Garak tool with prompt injection using specified probes.

    Parameters:
    model_type (str): The type of the model (e.g., "huggingface").
    model_name (str): The name of the model (e.g., "gpt2").
    probe_family (str): The family of the probe (e.g., "promptinject").
    probe (str): The probe to be used (e.g., "HijackHateHumans").
    """
    # Validate that the probe belongs to the specified family
    if probe not in PROBE_FAMILIES.get(probe_family, []):
        print(f"Invalid probe {probe} for family {probe_family}")
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
        f"{probe_family}.{probe}",
    ]

    try:
        completed_process = subprocess.run(
            command, check=True, capture_output=True, text=True
        )
        print("Return code:", completed_process.returncode)
        print("Standard Output:\n{}".format(completed_process.stdout))
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command. Error: {e}")


# Example usage:
promptinjection("huggingface", "gpt2", "promptinject", "HijackHateHumans")


def list_probes():
    """
    List available probes for prompt injection.
    """
    # Dummy example; replace with actual logic to list probes if necessary
    probes = ["dan.Dan_11_0", "dan.Dan_11_1", "dan.Dan_11_2"]
    print("Available probes for prompt injection:")
    for probe in probes:
        print(f"- {probe}")
