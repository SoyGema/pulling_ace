# inside cli.py

import argparse

from .attacks.tomato_attack import perform_tomato_attack
from .utils.subprocessor import promptinjection, run_injections, riskcards, toxicity
from .utils.subprocessor import promptinjection, run_injections, riskcards, toxicity


def main():
    parser = argparse.ArgumentParser(description="PullingAce.")
    subparsers = parser.add_subparsers(dest="command")

    parser.add_argument("--attack", type=str, help="Attack type")
    parser.add_argument("--model", type=str, help="Model to use")
    parser.add_argument("--dataset", type=str, help="Dataset to use")
    parser.add_argument(
        "--num-examples", type=int, default=10, help="Number of examples for the attack"
    )  # New argument

    # New parser for subprocessor
    subprocess_parser = subparsers.add_parser("prompt_injection")
    subprocess_parser.add_argument(
        "--model_type", type=str, required=True, help="Model type for subprocessor"
    )
    subprocess_parser.add_argument(
        "--model_name", type=str, required=True, help="Model name for subprocessor"
    )
    subprocess_parser.add_argument(
        "--probes", type=str, required=True, help="Probes for subprocessor"
    )

    subprocess_parser = subparsers.add_parser("riskcards")
    subprocess_parser.add_argument(
        "--model_type", type=str, required=True, help="Model type for subprocessor"
    )
    subprocess_parser.add_argument(
        "--model_name", type=str, required=True, help="Model name for subprocessor"
    )
    subprocess_parser.add_argument(
        "--probes", type=str, required=True, help="Probes for subprocessor"
    )

    subprocess_parser = subparsers.add_parser("toxicity")
    subprocess_parser.add_argument(
        "--model_type", type=str, required=True, help="Model type for subprocessor"
    )
    subprocess_parser.add_argument(
        "--model_name", type=str, required=True, help="Model name for subprocessor"
    )
    subprocess_parser.add_argument(
        "--probes", type=str, required=True, help="Probes for subprocessor"
    )

    args = parser.parse_args()

    #run_injections(args.model_type, args.model_name, args.probe_family)

    if args.attack == "tomato":
        results = perform_tomato_attack(args.model, args.dataset, args.num_examples)
        print(results)
    elif args.command == "prompt_injection":
        promptinjection(args.model_type, args.model_name, args.probes)
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
        print("Invalid command or no command specified")

if __name__ == "__main__":
    main()










