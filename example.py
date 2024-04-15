import torch
import json

from transformers import AutoTokenizer, AutoModelForCausalLM


def build_prompt(item):
    context = item['context']
    question = item['question']
    options = '\n'.join([key + '. ' + str(value) for key, value in item['options'].items()])

    prompt = f"According to following context answer question.\n\n"
    prompt += f"Context:\n{context}\n\n"
    prompt += f"Question:\nBased on the description above, {question}?\n\n"
    prompt += f"Options:\n{options}\n\n"
    prompt += "Please answer this question with JSON format, for example {\"option\":\"A\"}.\n"
    prompt += f"Answer:\n"

    return prompt


data_path = "marathon.json"

with open(data_path, "r") as f:
    data = json.load(f)

item = data[0]
prompt = build_prompt(item)

model_name_or_path = "01-ai/Yi-34B-200K"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

model = AutoModelForCausalLM.from_pretrained(
    pretrained_model_name_or_path=model_name_or_path,
    torch_dtype=torch.bfloat16,
    device_map='auto',
).eval()

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
)

answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
