<h2 align="center" style="font-size: 2.5em; font-weight: bold; color: #2c3e50;">
  <i>COIG-Writer</i>: A High-Quality Dataset for Chinese Creative Writing with Thought Processes
</h2>

This repository contains the dataset and supplementary materials for the paper **COIG-Writer: A High-Quality Dataset for Chinese Creative Writing with Thought Processes**.

---

## 🔔 Introduction

<p align="center">
  <img src="images/DataCuration.png" alt="COIG-Writer Overview" style="width: 800px;"> 
</p>

**COIG-Writer** is a large-scale Chinese creative writing dataset that connects final literary works with their underlying reasoning processes.  
Each sample includes a **reverse-engineered writing prompt**, a **step-by-step reasoning trace**, and the **final article**.  
This design allows researchers to explore *process-level creative reasoning* rather than only text-level output.

The dataset contains **1,665** triplets covering **51** genres, including novels, essays, scripts, and poetry.  
Data were curated through systematic reverse engineering and manually validated to ensure narrative coherence and creative depth.

**Key Insights**
- Process supervision stabilizes generation when balanced with general data at a **1:12** ratio.  
- Creative ability is **language-specific**, showing limited cross-lingual transfer.  
- Higher lexical diversity (**TTR**) does not necessarily imply higher creativity.

---

## 🏆 Dataset Statistics

| Metric | Value |
|---|---|
| Total Triplets | 1,665 |
| Total Genres | 51 |
| Prompt Length (min / avg / max) | 30 / 283 / 2,642 |
| Reasoning Length (min / avg / max) | 252 / 1,089 / 4,094 |
| Article Length (min / avg / max) | 12 / 2,214 / 31,071 |

**Genre Distribution**

| Category | Count | Share |
|---|---:|---:|
| Communication Writing | 481 | 28.9% |
| Novel | 467 | 28.0% |
| Non-fiction | 243 | 14.6% |
| Functional Writing | 221 | 13.3% |
| Poetry | 128 | 7.7% |
| Funny Literature | 68 | 4.1% |
| Script | 57 | 3.4% |

---

## ⚙️ Installation & Usage

To download and explore the dataset:

```bash
git clone https://anonymous.4open.science/r/COIG-Writer
cd COIG-Writer
```

You can also load it directly from Hugging Face:

```python
from datasets import load_dataset
dataset = load_dataset("COIG-Writer")
print(dataset["train"][0])
```

---

## 📦 Dataset Format

Each record in **COIG-Writer** follows the triplet structure below:

```json
{
  "id": "d6544671-d025-4832-a5f9-7fe261a290bf",
  "query": "请帮我以现代诗的形式创作一首关于山居与人间生活的对比作品，要求：\n\n使用山花、蜜蜂、蝴蝶等自然意象\n\n包含'寻找不能耕种的岩石'的哲学隐喻\n\n展现黄昏下山时的人间烟火气\n\n结尾通过'山中寒夜'与'人间空缺'形成双重对照\n\n语言简洁但富有画面感，适当使用通感（如蜜蜂的轰鸣）\n\n分三至四节，每节4-6行。",
  "thought": "主题是山居和人间生活的对比。首先，需要明确要求，确保每个点都覆盖到。问题提到了自然意象，比如山花、蜜蜂、蝴蝶，还有哲学隐喻“寻找不能耕种的岩石”，黄昏下山的人间烟火气，以及结尾的双重对照“山中寒夜”和“人间空缺”。语言要简洁但有画面感，用通感，比如蜜蜂的轰鸣。分三到四节，每节4-6行。……",
  "answer": "山中\n有时需要去山中，尤其在春天。\n离开人类，去寻找草木和鸟，\n离开人的平地，\n寻找不能耕种、不能居住的岩石。\n\n山花像一万年前一样盛开，\n仿佛不曾中断过。\n树随意生长，更接近太阳。\n寂静之中，一只蜜蜂过去，\n发出直升机般的轰鸣。\n蝴蝶过去的时候保持沉默。\n\n在黄昏走下山，走近人间。\n千万种声音从那里升起，\n聚成无法散去的云。\n\n在人间，人的居所等待着他，\n他没有做完的事，\n几个需要他的人。\n他需要填补自己留下的小小空缺。\n而山中的夜晚是冷的。\n"
}
```

**Field Descriptions**
- `id`: A unique UUID identifying each sample.  
- `query`: The reverse-engineered creative writing instruction that motivates the piece.  
- `thought`: The step-by-step reasoning process describing the writer’s conceptual and structural planning.  
- `answer`: The final completed literary text corresponding to the reasoning trace.  

Each triplet (`query`, `thought`, `answer`) captures **prompt-level intent**, **reasoning-level planning**, and **output-level realization**, enabling detailed research into *process-supervised creative generation*.

---

## 📜 License

**COIG-Writer** is distributed under the [Open Data Commons Attribution License (ODC-BY)](https://opendatacommons.org/licenses/by/).  
When using this dataset, please provide proper attribution.


