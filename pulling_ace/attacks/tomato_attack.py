"""
Script Name: Text Attack with Albert Model Using Tomato Swap
Author: Your Name
Date: Current date
Version: 1.0
License: MIT (or your chosen license)

Description:
This script performs adversarial attacks on a pre-trained Albert-base model using the TextAttack library. Specifically, it employs a 'Tomato Swap' attack. In this attack, a certain word from the input text is systematically replaced with the word 'tomato.' The objective is to mislead the model into making an incorrect classification while retaining the input's semantic meaning.

The attack strategy uses the following components:
- Goal Function: Untargeted Classification
- Transformation: Custom 'Tomato Swap'
- Constraints: No repeat modification, no stopword modification
- Search Method: Greedy Search


Dependencies:
- TextAttack
- Transformers
- Torch
- tqdm

Usage:
via cli after installing the library

Notes:
- Make sure to have sufficient computational resources, as running attacks can be resource-intensive.
"""
# inside tomato_attack_Albert.py

from textattack import Attack, AttackArgs, Attacker
from textattack.constraints.pre_transformation import (
    RepeatModification,
    StopwordModification,
)
from textattack.datasets import HuggingFaceDataset
from textattack.goal_functions import UntargetedClassification
from textattack.models.wrappers import HuggingFaceModelWrapper
from textattack.search_methods import GreedySearch
from textattack.transformations import WordSwap

from ..utils.pulling_ace_models import load_model_classification, load_tokenizer


class TomatoWordSwap(WordSwap):
    def _get_replacement_words(self, word):
        return ["tomato"]


def perform_tomato_attack(model_name, dataset_name, num_examples):
    model = load_model_classification(model_name)
    tokenizer = load_tokenizer(model_name)

    model_wrapper = HuggingFaceModelWrapper(model, tokenizer)
    goal_function = UntargetedClassification(model_wrapper)

    dataset = HuggingFaceDataset(dataset_name, None, "test")

    transformation = TomatoWordSwap()
    constraints = [RepeatModification(), StopwordModification()]

    search_method = GreedySearch()
    attack = Attack(goal_function, constraints, transformation, search_method)

    attack_args = AttackArgs()
    attacker = Attacker(attack, dataset, attack_args)
    attack_results = attacker.attack_dataset()

    return attack_results
