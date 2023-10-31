"""
Script Name: Text Attack with Falcon Model Using Tomato Swap
Author: Your Name
Date: Current date
Version: 1.0
License: MIT (or your chosen license)

Description:
This script performs adversarial attacks on a pre-trained Falcon-7b-instruct model using the TextAttack library. Specifically, it employs a 'Tomato Swap' attack. In this attack, a certain word from the input text is systematically replaced with the word 'tomato.' The objective is to mislead the model into making an incorrect classification while retaining the input's semantic meaning.

The attack strategy uses the following components:
- Goal Function: Untargeted Classification
- Transformation: Custom 'Tomato Swap'
- Constraints: No repeat modification, no stopword modification
- Search Method: Greedy Search

The Falcon model is assessed for its robustness against these adversarial examples using the SST-2 dataset, which is a binary classification dataset.

Dependencies:
- TextAttack
- Transformers
- Torch
- tqdm

Usage:
Run this script with Python 3.x. Make sure you have installed all required libraries.
To execute the script, run:
    python your_script_name.py

Notes:
- Make sure to have sufficient computational resources, as running attacks can be resource-intensive.
"""
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

from beyond_the_nest.beyond_the_nest.utils.beyond_the_nest_models import (
    load_falcon_model_classification,
    load_tokenizer,
)

# from tqdm import tqdm


class TomatoWordSwap(WordSwap):
    """Transforms an input by replacing any word with 'banana'."""

    # We don't need a constructor, since our class doesn't require any parameters.

    def _get_replacement_words(self, word):
        """Returns 'tomato', no matter what 'word' was originally.

        Returns a list with one item, since `_get_replacement_words` is intended to
            return a list of candidate replacement words.
        """
        return ["tomato"]


falcon = load_falcon_model_classification("tiiuae/falcon-7b-instruct")
# falcon2 = falcon.to_bettertransformer()
tokenizer = load_tokenizer("tiiuae/falcon-7b-instruct")
tokenizer.pad_token = tokenizer.eos_token


if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({"pad_token": "[PAD]"})
    falcon.resize_token_embeddings(len(tokenizer))


model_wrapper = HuggingFaceModelWrapper(falcon, tokenizer)
goal_function = UntargetedClassification(model_wrapper)

### Unclear if this dataset is going to work with falcon
dataset = HuggingFaceDataset("sst2", None, "test")


transformation = TomatoWordSwap()
constraints = [RepeatModification(), StopwordModification()]

search_method = GreedySearch()
attack = Attack(goal_function, constraints, transformation, search_method)

print(attack)

attack_args = AttackArgs(num_examples=10)
attacker = Attacker(attack, dataset, attack_args)
attack_results = attacker.attack_dataset()

print(attack_results)
