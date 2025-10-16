# *COIG-Writer*: A High-Quality Dataset for Chinese Creative Writing with Thought Processes

[🌐 Homepage](https://coig-writer.github.io/) · [🤗 Dataset](TODO) · [📖 ArXiv](TODO) · [🐙 GitHub](https://github.com/Juno6222222/COIG-Writer)

This repository contains the dataset and evaluation code for the paper **COIG-Writer: A High-Quality Dataset for Chinese Creative Writing with Thought Processes**.

---

## 🔔 Introduction

![COIG-Writer Overview](images/DataCuration.png)

**COIG-Writer** is a Chinese creative writing dataset that pairs final texts with their reasoning traces. Each sample is a triplet: a **reverse-engineered prompt**, a **reasoning process**, and the **final article**. The dataset contains **1,665** triplets across **51** genres and supports process-supervised training for narrative planning, style control, and instruction following.

Empirical findings:
- Process supervision stabilizes gains when combined with general data at a **1:12** ratio.  
- Creative ability is **language-specific** with limited cross-lingual transfer.  
- Higher lexical diversity (**TTR**) does not always reflect better creative quality.

---

## 🏆 Main Result

**Dataset Statistics**

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

## 🔢 Dataset Format

Each record is stored as a JSON object:

```json
{
  "reverse_inspiration_prompt": "<prompt>",
  "reasoning_process": "<step-by-step reasoning>",
  "article": "<final text>",
  "metadata": {
    "genre": "fantasy_novel",
    "quality_score": 55,
    "creativity_score": 9
  }
}
```

**Fields**
- **reverse_inspiration_prompt**: reconstructed writing instruction that could yield the article.  
- **reasoning_process**: planning steps and decisions.  
- **article**: final text.  
- **metadata**: genre and human ratings.

---

## ⚙️ Installation

```bash
git clone https://github.com/Juno6222222/COIG-Writer.git
cd COIG-Writer
pip install -r requirements.txt
```

---

## 🧠 Inference

```bash
export PYTHONPATH=$(pwd)

python infer/infer.py \
  --model_name <MODEL_NAME> \
  --input data/coig_writer_test.jsonl \
  --output results/pred.jsonl \
  --mode zero-shot \
  --batch_size 32
```

### Examples

```bash
# Zero-shot
python infer/infer.py --model_name Qwen2.5-7B-Instruct \
  --input data/coig_writer_test.jsonl \
  --output results/pred.jsonl \
  --mode zero-shot --batch_size 32

# Five-shot
python infer/infer.py --model_name DeepSeek-R1 \
  --input data/coig_writer_test.jsonl \
  --output results/pred.jsonl \
  --mode five-shot --batch_size 8
```

### Notes
- Interrupted runs save a `.jsonl.tmp` file for resuming.  
- After inference, check the `response` field and re-run for any errors.

### Custom Models
1. Add a new file under `infer/models/`.  
2. Register it in `infer/models/__init__.py`.

---

## ⭐ Evaluation

```bash
export PYTHONPATH=$(pwd)

python eval/eval.py \
  --reference data/coig_writer_test.jsonl \
  --prediction results/pred.jsonl \
  --save_dir results_with_status \
  --excel_output \
  --json_output
```

Evaluation covers content quality, creativity, cultural alignment, instruction adherence, and overall preference.

---

## 📜 License

**COIG-Writer** is released under the [Open Data Commons Attribution License (ODC-BY)](https://opendatacommons.org/licenses/by/). Please give proper attribution when using the dataset.

---

## 📚 Citation

```bibtex
@misc{coigwriter2025,
  title        = {COIG-Writer: A High-Quality Dataset for Chinese Creative Writing with Thought Processes},
  author       = {Yunwen Li and Shuangshuang Ying and Xingwei Qu and Xin Li and Sheng Jin and Minghao Liu and Zhoufutu Wen and Tianyu Zheng and Xeron Du and Qiguang Chen and Jiajun Shi and Wangchunshu Zhou and Jiazhan Feng and Wanjun Zhong and Chenghua Lin and Eli Zhang},
  year         = {2025},
  eprint       = {TODO},
  archivePrefix= {arXiv},
  primaryClass = {cs.CL},
  url          = {TODO}
}

