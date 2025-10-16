<h2 align="center" style="font-size: 2.5em; font-weight: bold; color: #2c3e50;"> <i>COIG-Writer</i>: A High-Quality Dataset for Chinese Creative Writing with Thought Processes </h2> <p align="center"> <a href="https://coig-writer.github.io/" style="margin: 0 10px;">🌐 Homepage</a> | <a href="TODO" style="margin: 0 10px;">🤗 Dataset</a> | <a href="TODO" style="margin: 0 10px;">📖 ArXiv</a> | <a href="TODO" style="margin: 0 10px;">🏆 Leaderboard</a> | <a href="https://github.com/Juno6222222/COIG-Writer" style="margin: 0 10px;">🐙 GitHub</a> </p>

This repository contains the dataset and evaluation code for the paper "COIG-Writer: A High-Quality Dataset for Chinese Creative Writing with Thought Processes
".

🔔 Introduction
<p align="center"> <img src="images/main_final.png" alt="COIG-Writer Overview" style="width: 800px;"> </p>

COIG-Writer is a Chinese creative writing dataset that pairs final texts with their reasoning traces. Each sample is a triplet: a reverse-engineered prompt, a detailed reasoning chain, and the final article. The dataset contains 1,665 triplets across 51 genres. It supports process-supervised learning for narrative planning, style control, and instruction following. Empirical analysis shows that (1) combining process data with general text at about 1:12 helps stabilize gains, (2) creative ability is language-specific with limited cross-lingual transfer, and (3) higher lexical diversity (TTR) does not always correlate with better creative quality.

🏆 Main Result

The table below summarizes basic statistics of COIG-Writer and highlights its coverage in genre and length ranges. These statistics help researchers select subsets and compare training or evaluation settings.

Dataset Statistics

Metric	Value
Total triplets	1,665
Total genres	51
Prompt length (min / avg / max)	30 / 283 / 2,642
Reasoning length (min / avg / max)	252 / 1,089 / 4,094
Article length (min / avg / max)	12 / 2,214 / 31,071

Category Distribution (Top-level)

Category	Count	Share
Communication Writing	481	28.9%
Novel	467	28.0%
Non-fiction	243	14.6%
Functional Writing	221	13.3%
Poetry	128	7.7%
Funny Literature	68	4.1%
Script	57	3.4%
🔢 Dataset Format

Each item is a JSON triplet:

{
  "reverse_inspiration_prompt": "<prompt>",
  "reasoning_process": "<step-by-step planning and decisions>",
  "article": "<final text>",
  "metadata": {
    "genre": "fantasy_novel",
    "quality_score": 55,
    "creativity_score": 9
  }
}

⚙️ Installation

To install the required packages, run:

# Prepare repository and environment
git clone https://github.com/Juno6222222/COIG-Writer.git
cd ./COIG-Writer
pip install -r requirements.txt

🧠 Inference

You can run generation with your model and then evaluate:

export PYTHONPATH=$(pwd)

# Local / API model inference (example)
python infer/infer.py \
  --model_name <MODEL_NAME> \
  --input data/coig_writer_test.jsonl \
  --output results/pred.jsonl \
  --mode zero-shot \
  --batch_size 32


Example:

export PYTHONPATH=$(pwd)

# Zero-shot with a local chat model
python infer/infer.py --model_name Qwen2.5-7B-Instruct --input data/coig_writer_test.jsonl --output results/pred.jsonl --mode zero-shot --batch_size 32

# Five-shot with a reasoning model
python infer/infer.py --model_name DeepSeek-R1 --input data/coig_writer_test.jsonl --output results/pred.jsonl --mode five-shot --batch_size 8


Parameter Explanations

model_name: local or API model identifier.

mode: zero-shot or five-shot.

batch_size: batch for local inference (for API mode use worker control in the script).

Other optional flags are documented in infer/infer.py.

📝 Notes

If inference stops unexpectedly, the script writes a temporary .jsonl.tmp. You can rerun to resume.

After inference, check the response field. If errors appear, rerun for those samples.

🛠️ Custom Model

Add a new file under infer/models/ and register it in infer/models/__init__.py.

⭐ Evaluation

After inference, run parsing and scoring:

export PYTHONPATH=$(pwd)

# Evaluate results (automatic + optional human templates)
python eval/eval.py \
  --reference data/coig_writer_test.jsonl \
  --prediction results/pred.jsonl \
  --save_dir results_with_status \
  --excel_output --json_output

📜 License

COIG-Writer is released under the Open Data Commons Attribution License (ODC-BY)
.
Please give appropriate credit when using the dataset and respect any licenses of referenced materials if you integrate external data.

📚 Citation

BibTeX:

@misc{coigwriter2025,
  title        = {COIG-Writer: A High-Quality Dataset for Chinese Creative Writing with Thought Processes},
  author       = {Yunwen Li and Shuangshuang Ying and Xingwei Qu and Xin Li and Sheng Jin and Minghao Liu and Zhoufutu Wen and Tianyu Zheng and Xeron Du and Qiguang Chen and Jiajun Shi and Wangchunshu Zhou and Jiazhan Feng and Wanjun Zhong and Chenghua Lin and Eli Zhang},
  year         = {2025},
  eprint       = {TODO},
  archivePrefix= {arXiv},
  primaryClass = {cs.CL},
  url          = {TODO}
}
