# Marathon: A Race Through the Realm of Long Context with Large Language Models

###### Paper coming soon ~

## Dataset Summary

Marathon benchmark is a new long-context multiple-choice benchmark, mainly based on [LooGLE](https://github.com/bigai-nlco/LooGLE), with some original data from [LongBench](https://github.com/THUDM/LongBench). The context length can reach up to 200K+. Marathon benchmark comprises six tasks: *Comprehension and Reasoning*, *Multiple Information Retrieval*, *Timeline Reorder*, *Computation*, *Passage Retrieval*, and *Short Dependency Question Answering*. Each test case includes a Long Context, a question, and multiple candidate options. Large Language Models (LLMs) need to select the correct answer from the given options based on the Long Context in the test.



## HuggingFace Dataset

Marathon is also available at Hugging Face dataset: [Marathon](https://huggingface.co/datasets/Lemoncoke/Marathon).



## Data Instances

An example of test looks as follows. This is a toy example.

```json
{
	"id": "7",
  "type": "comprehension_and_reasoning",
  "context": " Early life. Picardo was born in Jerez de la Frontera, in the Province of Cádiz in Andalucía, Spain on 18 June 1919. His father was Alvaro Picardo de Celis and his mother's family name was Castellón. He had four brothers, one of whom died in infancy. His father died in 1929 when Picardo was ten years old. With his mother and his brothers he moved to Madrid, Spain. [Truncated for display purpose] ",
  "question": "How many people were in Picardo's family when he was twelve?",
  "options": {
    "A": "five",
    "B": "eight",
    "C": "nine",
    "D": "ten"
  },
  "length": 268760
}
```



# Leaderboard

+ Methods (optimizing methods):
  + Vanilla
  + RAG (Retrieval Augmented Generation) 
  + PC (LongLLMLingua Prompt Compression)
+ Embedding Models:
  + OpenAI: text-embedding-ada-002
  + Jina: Jina-Embedding-base

|    Model     |Paramters | Context Window | Method | Embedding | Avg. Accuracy |
| :----------  |:----: | :----: | :----: | :-------: | :-----------: |
| **GPT-4**  | - | 128K  |  Vanilla   |   -    |     **78.59**     |
| Yi-chat  | 34B | 200K  |  RAG   |   Jina    |     63.81     |
| Yi-chat  | 34B | 200K  |  RAG   |  OpenAI   |     63.56     |
| Tutu2-DPO | 70B | 8K | RAG | OpenAI | 61.97 |
| Tutu2-DPO | 70B | 8K | RAG | Jina | 61.52 |
| Qwen | 14B | 8K | RAG | Jina |58.12|
| **ChatGPT** | - | 16K | Vanilla | - |**57.37**|
| Yi-chat  | 34B | 200K | Vanilla | - | 55.91 |
| Beluga2 | 70B | 4K | RAG | Jina |55.72|
| ChatGLM3  | 6B | 32K | Vanilla | - | 55.05 |
| Zephyr | 7B | 32K | RAG | Jina |53.79|
| Qwen | 14B | 8K | RAG | OpenAI |53.46|
| Beluga2 | 70B | 4K | PC | - |52.29|
| Mistral | 7B | 32K | RAG | Jina |52.04|
| Alfred | 40B | 8K | RAG | OpenAI |51.35|
| Alfred | 40B | 8K | RAG | Jina |51.24|
| ChatGLM3 | 6B | 32K | RAG | OpenAI |50.99|
| ChatGLM3 | 6B | 32K | RAG | Jina |50.60|
| Mistral | 7B | 32K | RAG | OpenAI |50.18|
| Zephyr | 7B | 32K | RAG | - |49.63|
| Beluga2  | 70B | 4K | Vanilla | - | 49.51 |
| Yi | 34B | 200K | PC | - |48.66|
| Beluga2 | 70B | 4K | RAG | OpenAI |48.24|
| ChatGLM3  | 6B | 32K | PC | - | 47.91 |
| Tulu2-DPO | 70B | 8K | PC | - |46.56|
| Qwen | 14B | 8K | PC | - |44.12|
| Mistral   | 7B | 32K | Vanilla | - | 39.81 |
| Qwen    | 14B | 8K | Vanilla | - | 39.27 |
| Alfred | 40B | 8K | PC | - |38.82|
| Zephyr    | 7B | 32K | Vanilla | - | 37.97 |
| Tulu2-DPO | 7B | 8K | Vanilla | - | 37.92 |
| Longchat | 13B | 16K | RAG | Jina |37.78|
| Alfred   | 40B | 8K | Vanilla | - | 37.31 |
| Mistral   | 7B | 32K | PC | - | 37.01 |
| Longchat | 13B | 16K | Vanilla | - | 35.87 |
| Longchat | 13B | 16K | PC | - | 35.61 |
| Zephyr    | 7B | 32K | PC | - | 30.23 |
| Longchat | 13B | 16K | RAG | OpenAI |29.95|



## Online Evaluation

Welcome to Marathon Race, online evaluation is now available at [https://openbenchmark.online/marathon](https://openbenchmark.online/marathon).

**Answer File Format**

The file should be a JSON file containing a list of dictionaries with a length of 1530. Each dictionary must include at least two fields: 'id' and 'answer'. Here is a sample answer file:

```json
[
  {
    "id": "0",
    "answer": "C"
  },
  {
    "id": "1",
    "answer": "B"
  },
  {
    "id": "2",
    "answer": "B"
  },
  ...
   {
    "id": "1529",
    "answer": "C"
  }
]
```

**Results File Format**

The Results file is a JSON file that includes the accuracy of the LLM (Language Learning Model) in 6 tasks within the Marathon, as well as the average accuracy across all tasks. Here is a sample results file:

```json
{
    "comprehension_and_reasoning": {
        "accuracy": 0.46218487394957986,
        "correct": 165,
        "total": 357
    },
    "multiple_information_retrieval": {
        "accuracy": 0.41935483870967744,
        "correct": 143,
        "total": 341
    },
    "timeline_reorder": {
        "accuracy": 0.2894736842105263,
        "correct": 44,
        "total": 152
    },
    "computation": {
        "accuracy": 0.23711340206185566,
        "correct": 23,
        "total": 97
    },
    "passage_retrieval": {
        "accuracy": 0.49666666666666665,
        "correct": 149,
        "total": 300
    },
    "shortdep_qa": {
        "accuracy": 0.4840989399293286,
        "correct": 137,
        "total": 283
    },
    "average": 0.39814873425460573
}
```



## Citations

If you find our work useful, please cite us.

```
@article{zhang2023marathon,
  title={Marathon: A Race Through the Realm of Long Context with Large Language Models},
  author={Zhang, Lei and Li, Yunshui and Liu, Ziqiang and Liu, Junhao and Yang, Jiaxi and Yang, Min},
  url={https://huggingface.co/datasets/Lemoncoke/Marathon},
  year={2023}
}
```

When citing our work, please kindly consider citing the original dataset papers.

```
@misc{li2023loogle,
  title={Can Long-Context Language Models Understand Long Contexts?},
  author={ Li, Jiaqi and Wang, Mengmeng and Zheng, Zilong and Zhang, Muhan },
  url={https://github.com/bigai-nlco/LooGLE},
  year={2023}
}
```

```
@article{bai2023longbench,
  title={LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding},
  author={Bai, Yushi and Lv, Xin and Zhang, Jiajie and Lyu, Hongchang and Tang, Jiankai and Huang, Zhidian and Du, Zhengxiao and Liu, Xiao and Zeng, Aohan and Hou, Lei and Dong, Yuxiao and Tang, Jie and Li, Juanzi},
  journal={arXiv preprint arXiv:2308.14508},
  year={2023}
}
```

