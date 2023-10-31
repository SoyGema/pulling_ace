# inside cli.py

# This file contains the command-line interface for the PullingAce module.
# It imports the necessary modules and defines the main function for executing the tomato attack.

import argparse

from .attacks.tomato_attack import perform_tomato_attack


def main():
    parser = argparse.ArgumentParser(description="PullingAce.")
    parser.add_argument("--attack", type=str, help="Attack type")
    parser.add_argument("--model", type=str, help="Model to use")
    parser.add_argument("--dataset", type=str, help="Dataset to use")
    parser.add_argument(
        "--num-examples", type=int, default=10, help="Number of examples for the attack"
    )  # New argument

    args = parser.parse_args()

    if args.attack == "tomato":
        results = perform_tomato_attack(args.model, args.dataset, args.num_examples)
        print(results)


if __name__ == "__main__":
    main()
# inside cli.py

# This file contains the command-line interface for the PullingAce module.
# It imports the necessary modules and defines the main function for executing the tomato attack.

import argparse

from .attacks.tomato_attack import perform_tomato_attack


def main():
    parser = argparse.ArgumentParser(description="PullingAce.")
    parser.add_argument("--attack", type=str, help="Attack type")
    parser.add_argument("--model", type=str, help="Model to use")
    parser.add_argument("--dataset", type=str, help="Dataset to use")
    parser.add_argument(
        "--num-examples", type=int, default=10, help="Number of examples for the attack"
    )  # New argument

    args = parser.parse_args()

    if args.attack == "tomato":
        results = perform_tomato_attack(args.model, args.dataset, args.num_examples)
        print(results)


if __name__ == "__main__":
    main()
