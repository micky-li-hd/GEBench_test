# GUI Agent - Text-to-GUI Generation & Evaluation Toolkit

A lightweight toolkit for generating and evaluating GUI screenshots using Gemini API and GPT-4o for assessment.

<div align="center">

[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/abs/YOUR_PAPER_ID)
[![Project Page](https://img.shields.io/badge/Project-Page-blue)](YOUR_PROJECT_PAGE_URL)
[![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-green)](https://huggingface.co/datasets/stepfun-ai/GEBench)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Task: GUI Generation](https://img.shields.io/badge/Task-GUI%20Generation-1E90FF)

</div>

![Benchmark Comparison](./assets/teaser.jpg)

## Features

- **5 Data Types**: Type 1 (single-step), Type 2 (multi-step), Type 3 (text-fictionalapp), Type 4 (text-realapp), Type 5 (grounding)
- **Bilingual Support**: Automatic Chinese/English prompt selection based on folder naming
- **5-Dimensional Metrics**: goal, logic, consistency, ui, quality

## Dataset

The GEBench dataset is available on HuggingFace:

📊 **[stepfun-ai/GEBench](https://huggingface.co/datasets/stepfun-ai/GEBench)** - HuggingFace Datasets Hub

To download:
```bash
from datasets import load_dataset
dataset = load_dataset("stepfun-ai/GEBench")
```

Or use Git LFS:
```bash
git clone https://huggingface.co/datasets/stepfun-ai/GEBench
cd GEBench
git lfs pull
```

## Quick Start

### Installation

```bash
git clone https://github.com/micky-li-hd/GEBench_test.git
cd GEBench_test/code
pip install -e .
```

### Generate Images

```bash
python scripts/generate.py --data-type type1 --data-folder data/01_single_step --output-dir outputs/gemini --gemini-api-key YOUR_GEMINI_API_KEY
python scripts/generate.py --data-type type2 --data-folder data/02_multi_step --output-dir outputs/gemini --gemini-api-key YOUR_GEMINI_API_KEY
python scripts/generate.py --data-type type3 --data-folder data/03_trajectory_text_fictionalapp --output-dir outputs/gemini --gemini-api-key YOUR_GEMINI_API_KEY
python scripts/generate.py --data-type type4 --data-folder data/04_trajectory_text_realapp --output-dir outputs/gemini --gemini-api-key YOUR_GEMINI_API_KEY
python scripts/generate.py --data-type type5 --data-folder data/05_grounding_data --output-dir outputs/gemini --gemini-api-key YOUR_GEMINI_API_KEY

# With multiple workers
python scripts/generate.py --data-type type1 --data-folder data/01_single_step --output-dir outputs/gemini --gemini-api-key YOUR_GEMINI_API_KEY --workers 4
```

### Evaluate Results

```bash
python scripts/evaluate.py --data-type type1 --output-folder outputs/gemini/01_single_step --dataset-root data --openai-api-key YOUR_OPENAI_API_KEY
python scripts/evaluate.py --data-type type2 --output-folder outputs/gemini/02_multi_step --dataset-root data --openai-api-key YOUR_OPENAI_API_KEY
python scripts/evaluate.py --data-type type5 --output-folder outputs/gemini/05_grounding_data --dataset-root data --openai-api-key YOUR_OPENAI_API_KEY

# With multiple workers
python scripts/evaluate.py --data-type type1 --output-folder outputs/gemini/01_single_step --dataset-root data --openai-api-key YOUR_OPENAI_API_KEY --workers 4
```

## Project Structure

```
gui_agent/
├── generation/      # Type 1-5 generators + Gemini provider
├── evaluation/      # Type 1-5 judges + GPT-4o provider
├── api.py          # Generator & Evaluator classes
├── config.py       # Configuration
└── schemas.py      # Data models

scripts/
├── generate.py     # Image generation
└── evaluate.py     # Evaluation with GPT-4o
```

## Python API

```python
from gui_agent import Generator, GenerationConfig
from pathlib import Path

config = GenerationConfig(
    provider="gemini",
    api_key="your-api-key",
    output_dir=Path("outputs/gemini")
)

gen = Generator(config)
gen.generate(data_type="type1", data_folder=Path("data/01_single_step"))
```

```python
from gui_agent import Evaluator, EvaluationConfig
from pathlib import Path

config = EvaluationConfig(
    judge="gpt4o",
    api_key="your-api-key",
    dataset_root=Path("data")
)

evaluator = Evaluator(config)
results = evaluator.evaluate(
    data_type="type1",
    output_folder=Path("outputs/gemini/01_single_step")
)
```

## License

MIT License
