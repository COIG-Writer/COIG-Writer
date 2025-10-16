<h2 align="center" style="font-size: 2.5em; font-weight: bold; color: #2c3e50;">
  <i>COIG-Writer</i>: A High-Quality Dataset for Chinese Creative Writing with Thought Processes
</h2>

<p align="center">
  <a href="https://coig-writer.github.io/" style="margin: 0 10px;">🌐 Homepage</a> |
  <a href="https://huggingface.co/datasets/m-a-p/COIG-Writer" style="margin: 0 10px;">🤗 Dataset</a> |
  <a href="https://arxiv.org/abs/2503.xxxxx" style="margin: 0 10px;">📖 ArXiv</a> |
  <a href="https://github.com/Juno6222222/COIG-Writer" style="margin: 0 10px;">🐙 GitHub</a>
</p>

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
git clone https://github.com/Juno6222222/COIG-Writer.git
cd COIG-Writer
pip install -r requirements.txt
```

You can also load it directly from Hugging Face:

```python
from datasets import load_dataset
dataset = load_dataset("m-a-p/COIG-Writer")
print(dataset["train"][0])
```

---

## 📜 License

**COIG-Writer** is distributed under the [Open Data Commons Attribution License (ODC-BY)](https://opendatacommons.org/licenses/by/).  
When using this dataset, please provide proper attribution.

---

## 📚 Citation

```bibtex
@misc{coigwriter2025,
  title        = {COIG-Writer: A High-Quality Dataset for Chinese Creative Writing with Thought Processes},
  author       = {Yunwen Li and Shuangshuang Ying and Xingwei Qu and Xin Li and Sheng Jin and Minghao Liu and Zhoufutu Wen and Tianyu Zheng and Xeron Du and Qiguang Chen and Jiajun Shi and Wangchunshu Zhou and Jiazhan Feng and Wanjun Zhong and Chenghua Lin and Eli Zhang},
  year         = {2025},
  eprint       = {2503.xxxxx},
  archivePrefix= {arXiv},
  primaryClass = {cs.CL},
  url          = {https://arxiv.org/abs/2503.xxxxx}
}
```
