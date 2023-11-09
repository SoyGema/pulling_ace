# inside cli.py

import argparse

from .attacks.tomato_attack import perform_tomato_attack
from .utils.subprocessor import promptinjection, run_injections, riskcards, toxicity


def main():
    parser = argparse.ArgumentParser(description="PullingAce.")
    subparsers = parser.add_subparsers(dest="command")
    # Subparser for tomato attack
    tomato_parser = subparsers.add_parser("tomato")
    tomato_parser.add_argument("--model", type=str, required=True, help="Model to use")
    tomato_parser.add_argument("--dataset", type=str, required=True, help="Dataset to use")
    tomato_parser.add_argument("--num-examples", type=int, default=10, help="Number of examples for the attack")

    # Subparser for prompt injection attack
    prompt_injection_parser = subparsers.add_parser("promptinjection")
    prompt_injection_parser.add_argument("--model_type", type=str, required=True, help="Model type for subprocessor")
    prompt_injection_parser.add_argument("--model", type=str, required=True, help="Model name for subprocessor")
    prompt_injection_parser.add_argument("--probes", type=str, required=True, help="Probes for subprocessor")

    # ... (add other subparsers for riskcards, toxicity, etc.)
    toxicity_parser = subparsers.add_parser("toxicity")
    toxicity_parser.add_argument("--model_type", type=str, required=True, help="Model type for subprocessor")
    toxicity_parser.add_argument("--model", type=str, required=True, help="Model name for subprocessor")
    toxicity_parser.add_argument("--probes", type=str, required=True, help="Probes for subprocessor")

    # ... (add other subparsers for riskcards, toxicity, etc.)
    riskcards_parser = subparsers.add_parser("riskcards")
    riskcards_parser.add_argument("--model_type", type=str, required=True, help="Model type for subprocessor")
    riskcards_parser.add_argument("--model", type=str, required=True, help="Model name for subprocessor")
    riskcards_parser.add_argument("--probes", type=str, required=True, help="Probes for subprocessor")

    args = parser.parse_args()

    #if args.command == "tomato":
        #results = perform_tomato_attack(args.model, args.dataset, args.num_examples)
        #print(results)
    if args.command == "promptinjection":
        promptinjection(args.model_type, args.model, args.probes)
        #run_injections(args.model_type, args.model, "promptinject")

    elif args.command == "toxicity":
        toxicity(args.model_type, args.model, args.probes)
        #run_injections(args.model_type, args.model, "realtoxicityprompts")

    elif args.command == "riskcards":
        riskcards(args.model_type, args.model, args.probes)
        #run_injections(args.model_type, args.model, "lmrc")

    # ... (handle other subcommands)
    else:
        print("Invalid command or no command specified")

if __name__ == "__main__":
    main()





