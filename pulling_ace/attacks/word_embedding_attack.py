"""
This script implements a TextAttack adversarial attack on a given model.

Attack Components:
1. Goal Function:
   - UntargetedClassification: This function attempts to make the model's output incorrect. For classification, this means the output will be any class other than the original.

2. Transformation:
   - CompositeTransformation consisting of:
     a) WordSwapEmbedding: Swaps words with their embeddings, based on cosine similarity.
     b) WordSwapGradientBased: Uses the model's gradient to suggest the optimal word swaps.
     c) WordSwapNearestNeighbor: Swaps words with their nearest neighbors in the embedding space.
     d) WordSwapRandomCharacterInsertion: Randomly inserts a character into a word.
     e) WordSwapRandomCharacterSubstitution: Randomly substitutes a character within a word.
     f) WordSwapRandomCharacterDeletion: Randomly deletes a character from a word.

3. Constraints:
   a) MaxWordsPerturbed: Limits the number of words that can be perturbed in the text.
   b) RepeatModification: Ensures that the same word is not modified more than once.
   c) StopwordModification: Prevents the modification of stopwords, which are usually not meaningful in altering the sentence's sentiment.
4. Search Method:
   - GreedySearch: Starts with an original example and greedily chooses the best transformation from all available transformations until the goal function is satisfied or no transformations can be applied.

Usage:
Execute the script after setting up the model and dataset. Monitor the attack's success rate, accuracy under attack, and other metrics to understand the robustness of the model against the adversarial attack.

Note:
Experiment with different combinations of transformations, constraints, and search methods to find the most effective attack strategy for a given model and dataset.

"""
from textattack import Attack, AttackArgs, Attacker
from textattack.constraints.grammaticality import PartOfSpeech
from textattack.constraints.pre_transformation import (
    RepeatModification,
    StopwordModification,
)
from textattack.datasets import HuggingFaceDataset
from textattack.goal_functions import UntargetedClassification
from textattack.models.wrappers import HuggingFaceModelWrapper
from textattack.search_methods import GreedySearch
from textattack.transformations import WordSwapEmbedding

from ..utils.pulling_ace_models import load_model_classification, load_tokenizer


def perfom_word_embedding_attack(model_name, dataset_name):
    model = load_model_classification(model_name)
    # falcon2 = falcon.to_bettertransformer()
    tokenizer = load_tokenizer(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    model_wrapper = HuggingFaceModelWrapper(model, tokenizer)
    goal_function = UntargetedClassification(model_wrapper)

    ###
    dataset = HuggingFaceDataset(dataset_name, None, "test")

    ## TODO
    # from textattack.constraints.semantics.sentence_encoders.universal_sentence_encoder import UniversalSentenceEncoder

    transformation = WordSwapEmbedding(max_candidates=50)

    constraints = [RepeatModification(), StopwordModification(), PartOfSpeech()]

    search_method = GreedySearch()
    # OR, using Beam Search with a beam width of 5
    # search_method = BeamSearch(beam_width=5)

    attack = Attack(goal_function, constraints, transformation, search_method)

    print(attack)

    attack_args = AttackArgs(num_examples=10)
    attacker = Attacker(attack, dataset, attack_args)
    attack_results = attacker.attack_dataset()

    print(attack_results)
