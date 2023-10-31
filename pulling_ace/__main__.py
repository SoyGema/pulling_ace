import beyond_the_nest
from beyond_the_nest.beyond_the_nest import generate_text, load_transformers_model

# Example usage:
model_name = "tiiuae/falcon-7b-instruct"
text_gen_pipeline = load_transformers_model(model_name)

input_text = "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:"
generated_text = generate_text(text_gen_pipeline, input_text)

if __name__ == "__main__":
    generate_text
import beyond_the_nest

# Example usage:
model_name = "tiiuae/falcon-7b-instruct"
text_gen_pipeline = load_transformers_model(model_name)

input_text = "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:"
generated_text = generate_text(text_gen_pipeline, input_text)

if __name__ == "__main__":
    generate_text
