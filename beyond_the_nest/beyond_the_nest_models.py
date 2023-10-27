import torch
from transformers import AutoTokenizer, FalconForSequenceClassification, pipeline


def load_falcon_model_generation(model_name):
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize the text-generation pipeline
    text_gen_pipeline = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )

    return text_gen_pipeline


def load_falcon_model_classification(model_name):
    # load model for classification
    model = FalconForSequenceClassification.from_pretrained(model_name)
    return model


def load_tokenizer(model_name):
    return AutoTokenizer.from_pretrained(model_name)


def generate_text(
    model, input_text, max_length=200, do_sample=True, top_k=10, num_return_sequences=1
):
    result = model(
        input_text,
        max_length=max_length,
        do_sample=do_sample,
        top_k=top_k,
        num_return_sequences=num_return_sequences,
    )
    return result[0]["generated_text"]
