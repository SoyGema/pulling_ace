# inside cli.py

import argparse

from .attacks.tomato_attack import perform_tomato_attack
from .utils.subprocessor import promptinjection, run_injections


def main():
    """
    Main function to handle command line arguments and perform the requested operation.
    Arguments:
    --attack: Specifies the type of attack to perform.
    --model: Specifies the model to use for the attack.
    --dataset: Specifies the dataset to use for the attack.
    --num-examples: Specifies the number of examples to use for the attack. Default is 10.
    """
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

    args = parser.parse_args()


    if args.attack == "tomato":
        results = perform_tomato_attack(args.model, args.dataset, args.num_examples)
        print(results)
    elif args.command == "prompt_injection":
        run_injections(args.model_type, args.model_name, args.probes)
        promptinjection(args.model_type, args.model_name, args.probes)

    else:
        # inside cli.py
        
        import argparse
        
        from .attacks.tomato_attack import perform_tomato_attack
        from .utils.subprocessor import promptinjection, run_injections
        
        
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
            # New parser for subprocessor
            subprocess_parser = subparsers.add_parser("prompt_injection")
        =======
            # New parser for subprocessor
            # This parser is used to handle the "prompt_injection" command, which requires the "model_type", "model_name", and "probes" arguments.
            subprocess_parser = subparsers.add_parser("prompt_injection")
if __name__ == "__main__":
    main()
