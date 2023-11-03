from beyond_the_nest.beyond_the_nest.utils.beyond_the_nest_models import (
    load_falcon_model_classification,
    load_tokenizer,
)
from textattack.datasets import HuggingFaceDataset

falcon = load_falcon_model_classification("tiiuae/falcon-7b-instruct")
# falcon2 = falcon.to_bettertransformer()
tokenizer = load_tokenizer("tiiuae/falcon-7b-instruct")
tokenizer.pad_token = tokenizer.eos_token

num_classes_model = (
    falcon.config.num_labels
)  # Replace 'falcon' with your model variable
print(f"Number of classes in the model: {num_classes_model}")

dataset = HuggingFaceDataset("sst2", None, "test")


# Assuming `dataset` is a HuggingFaceDataset object
unique_labels = set()
for example in dataset:
    unique_labels.add(example["label"])

print(f"Number of classes in the dataset: {len(unique_labels)}")

print(f"Number of classes in the dataset: {len(unique_labels)}")
