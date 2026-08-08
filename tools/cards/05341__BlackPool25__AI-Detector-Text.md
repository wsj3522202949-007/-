---
id: tool-05341
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Detector-Text
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/blackpool25/ai-detector-text
created: 2026-07-18
updated: 2026-07-18
no: 5341
category: 一、去 AI 味 / Humanizer 库
repo: BlackPool25/AI-Detector-Text
stars: 0
url: https://github.com/blackpool25/ai-detector-text
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5c9c7bd301e13812
  - methods/改稿润色指令库.md
---

# BlackPool25/AI-Detector-Text

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/blackpool25/ai-detector-text
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：BlackPool25/AI-Detector-Text
- **拉取时间**：2026-07-25 18:15:00

---

# AI Text Detection Dataset Preprocessor

A production-grade Python script for processing large CSV datasets (millions of rows) with automatic schema detection, memory-efficient chunked processing, intelligent data segregation, and Parquet output optimization.

## Features

✨ **Automatic Schema Detection**: Fuzzy column matching for text, labels, models, domains, and attack types  
🚀 **Memory Efficient**: Processes datasets larger than available RAM using chunked iteration  
📊 **Real-time Analytics**: Live progress tracking with statistics and ETA  
💾 **Smart Checkpointing**: Resume processing from interruptions  
🎯 **Intelligent Segregation**: Automatically organizes data by label and model  
📦 **Parquet Optimization**: Efficient storage with Snappy/Gzip compression  
🔍 **Validation Mode**: Dry-run analysis before processing  
🛡️ **Robust Error Handling**: Continues processing even with problematic rows  

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone or download this repository:
```bash
cd /home/lightdesk/Projects/Text
```

2. (Optional but recommended) Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
ai-text-preprocessor/
├── src/                        # Source code
│   └── preprocessor/          # Main preprocessor module
│       ├── __init__.py
│       └── preprocess.py      # Core preprocessing script
├── scripts/                   # Utility scripts
│   ├── analyze_data.py        # Data analysis tools
│   └── validate_processed_data.py  # Output validation
├── tests/                     # Test suite
│   ├── __init__.py
│   └── test_preprocess.py     # Unit tests
├── examples/                  # Usage examples
│   └── usage_examples.py      # Code examples
├── docs/                      # Documentation
│   ├── GETTING_STARTED.md
│   ├── QUICKSTART.md
│   ├── IMPLEMENTATION_SUMMARY.md
│   ├── CHANGELOG.md
│   └── planning/              # Project planning docs
├── data/                      # Data directory
│   ├── raw/                   # Raw input datasets
│   ├── samples/               # Sample/test datasets
│   └── processed/             # Processed output (gitignored)
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── setup.py                   # Package installation script
└── .gitignore                 # Git ignore rules
```

## Quick Start

### 1. Validate Your Dataset (Recommended First Step)

Before processing, run validation to check your dataset structure:

```bash
python src/preprocessor/preprocess.py --input data/raw/your_data.csv --output data/processed --validate-only
```

This will:
- Detect the schema automatically
- Show sample data and statistics
- Identify potential issues
- Estimate processing time and output size

### 2. Process Your Dataset

Basic usage:
```bash
python src/preprocessor/preprocess.py --input data/raw/your_data.csv --output data/processed
```

Advanced usage with options:
```bash
python src/preprocessor/preprocess.py \
    --input data/raw/large_dataset.csv \
    --output data/processed \
    --chunk-size 50000 \
    --min-text-length 20 \
    --max-text-length 50000 \
    --compression gzip \
    --remove-duplicates
```

### 3. Resume Interrupted Processing

If processing is interrupted, resume from the last checkpoint:
```bash
python src/preprocessor/preprocess.py --input data/raw/your_data.csv --output data/processed --resume
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--input` | Path to input CSV file (required) | - |
| `--output` | Output directory path (required) | - |
| `--chunk-size` | Number of rows to process per chunk | 100000 |
| `--min-text-length` | Minimum text length to keep | 10 |
| `--max-text-length` | Maximum text length to keep | 100000 |
| `--compression` | Compression method: `snappy` or `gzip` | snappy |
| `--remove-duplicates` | Remove duplicate texts (default: enabled) | True |
| `--no-remove-duplicates` | Keep duplicate texts | - |
| `--resume` | Resume from checkpoint | False |
| `--validate-only` | Analyze schema without processing | False |
| `--threads` | Number of I/O threads | 4 |
| `--checkpoint-interval` | Save checkpoint every N chunks | 10 |

## Input CSV Requirements

Your CSV file should contain at least:

1. **Text Column**: Contains the text data
   - Matching patterns: `text`, `content`, `document`, `generation`, `passage`, `prompt`, `output`

2. **Label Column**: Contains the classification labels
   - Matching patterns: `label`, `class`, `is_ai`, `source`, `category`, `type`
   - Supported formats:
     - Binary numeric: `0, 1` (0=human, 1=ai)
     - Binary string: `human, ai` or `Human, AI`
     - Binary boolean: `true, false`
     - Multi-class: Model names like `gpt4`, `claude`, `human`

### Optional Columns

- **Model Column**: AI model name (e.g., `gpt4`, `claude`)
- **Domain Column**: Text domain/genre (e.g., `news`, `reddit`, `arxiv`)
- **Attack Column**: Adversarial attack type (if applicable)

### Example CSV Structure

```csv
text,label,model,domain
"This is human-written text.",human,human,news
"AI-generated content here.",ai,gpt4,articles
"Another example text.",ai,claude,reddit
```

## Output Structure

The script organizes processed data into a structured directory:

```
processed_data/
├── human/
│   ├── chunk_0001.parquet
│   ├── chunk_0002.parquet
│   └── metadata.json
├── ai/
│   ├── gpt4/
│   │   ├── chunk_0001.parquet
│   │   ├── chunk_0002.parquet
│   │   └── metadata.json
│   ├── claude/
│   │   ├── chunk_0001.parquet
│   │   └── metadata.json
│   └── gpt3.5/
│       └── chunk_0001.parquet
├── unknown/  (if any labels couldn't be classified)
│   └── chunk_0001.parquet
├── statistics.json
├── processing_log.txt
└── checkpoint.json
```

### Output Files

#### Parquet Files

Each Parquet file contains:
- `text`: The text content
- `label`: Binary label (0=human, 1=ai)
- `label_name`: Human-readable label ("human" or "ai")
- `model`: AI model name or "human"
- `domain`: Text domain/category
- `attack_type`: Attack type (if applicable)
- `text_length`: Character count
- `chunk_id`: Chunk number
- `row_id`: Original row index

#### Metadata Files

**statistics.json** (root directory):
```json
{
  "total_samples": 4900000,
  "human_samples": 149710,
  "ai_samples": 4750290,
  "ai_model_breakdown": {
    "gpt4": 523419,
    "gpt3.5": 612358,
    "claude": 445123
  },
  "processing_time_seconds": 3847,
  "original_csv_size_gb": 12.4,
  "output_size_gb": 2.1,
  "compression_ratio": 0.169
}
```

**metadata.json** (per model/label folder):
```json
{
  "label": "ai",
  "model_name": "gpt4",
  "total_samples": 523419,
  "num_chunks": 6,
  "date_processed": "2025-10-18T10:30:00Z"
}
```

## Loading Processed Data

### With Pandas

```python
import pandas as pd

# Load single file
df = pd.read_parquet('processed_data/human/chunk_0001.parquet')

# Load all human data
df_human = pd.concat([
    pd.read_parquet(f) 
    for f in Path('processed_data/human').glob('*.parquet')
])
```

### With HuggingFace Datasets

```python
from datasets import load_dataset

# Load all data
dataset = load_dataset('parquet', data_dir='processed_data')

# Load specific label
dataset_human = load_dataset('parquet', data_dir='processed_data/human')
dataset_ai_gpt4 = load_dataset('parquet', data_dir='processed_data/ai/gpt4')

# Create train/val/test splits
dataset = dataset['train'].train_test_split(test_size=0.2, seed=42)
test_valid = dataset['test'].train_test_split(test_size=0.5, seed=42)

final_dataset = {
    'train': dataset['train'],
    'validation': test_valid['train'],
    'test': test_valid['test']
}
```

### With PyArrow

```python
import pyarrow.parquet as pq

# Read single file
table = pq.read_table('processed_data/human/chunk_0001.parquet')
df = table.to_pandas()

# Read entire directory
dataset = pq.ParquetDataset('processed_data')
table = dataset.read()
```

## Performance Tips

### Memory Optimization

If you encounter memory issues:
1. Reduce chunk size: `--chunk-size 50000`
2. Close other applications
3. Process on a machine with more RAM

### Speed Optimization

To speed up processing:
1. Increase chunk size (if RAM allows): `--chunk-size 200000`
2. Use faster compression: `--compression snappy` (default)
3. Run on SSD storage
4. Disable duplicate removal if not needed: `--no-remove-duplicates`

### Disk Space

Required disk space is approximately 20-25% of the original CSV size when using Snappy compression, or 15-20% with Gzip compression.

## Troubleshooting

### "Could not detect text column"

The script couldn't identify your text column. Rename it to one of: `text`, `content`, `document`, `passage`, or `output`.

### "Could not detect label column"

Rename your label column to: `label`, `class`, `is_ai`, or `source`.

### High memory usage warning

Reduce the chunk size:
```bash
python src/preprocessor/preprocess.py --input data/raw/data.csv --output data/processed --chunk-size 50000
```

### Processing is too slow

Increase chunk size (if memory allows):
```bash
python src/preprocessor/preprocess.py --input data/raw/data.csv --output data/processed --chunk-size 200000
```

### Encoding errors

The script tries multiple encodings automatically (utf-8, latin-1, iso-8859-1, cp1252). If it still fails, convert your CSV to UTF-8 first.

## Data Cleaning Pipeline

The script automatically:
1. ✓ Strips whitespace from text
2. ✓ Removes null bytes
3. ✓ Normalizes UTF-8 encoding (NFKC)
4. ✓ Drops rows with missing text
5. ✓ Filters by text length
6. ✓ Removes exact duplicates (optional)
7. ✓ Normalizes labels to binary format
8. ✓ Adds computed columns (text_length, chunk_id, row_id)

## Advanced Features

### Checkpointing

Processing automatically saves checkpoints every 10 chunks (configurable). If interrupted, resume with:
```bash
python src/preprocessor/preprocess.py --input data/raw/data.csv --output data/processed --resume
```

### Custom Checkpoint Interval

```bash
python src/preprocessor/preprocess.py --input data/raw/data.csv --output data/processed --checkpoint-interval 5
```

### Validation Mode

Analyze your dataset before processing:
```bash
python src/preprocessor/preprocess.py --input data/raw/data.csv --output data/processed --validate-only
```

This provides:
- Schema detection results
- Sample data preview
- Label distribution
- Text length statistics
- Potential issues detection
- Processing time estimate

## Examples

### Example 1: Basic Processing

```bash
python src/preprocessor/preprocess.py \
    --input data/raw/my_dataset.csv \
    --output data/processed
```

### Example 2: High-Quality Processing

```bash
python src/preprocessor/preprocess.py \
    --input data/raw/dataset.csv \
    --output data/processed \
    --min-text-length 50 \
    --max-text-length 10000 \
    --compression gzip \
    --remove-duplicates
```

### Example 3: Memory-Constrained Environment

```bash
python src/preprocessor/preprocess.py \
    --input data/raw/large_dataset.csv \
    --output data/processed \
    --chunk-size 25000 \
    --checkpoint-interval 5
```

### Example 4: Fast Processing (RAM Available)

```bash
python src/preprocessor/preprocess.py \
    --input data/raw/dataset.csv \
    --output data/processed \
    --chunk-size 500000 \
    --no-remove-duplicates \
    --compression snappy
```

## Statistics and Monitoring

During processing, the script displays:
- Real-time progress bar with ETA
- Processing speed (rows/second)
- Memory usage
- Cumulative statistics:
  - Total rows processed
  - Human vs AI distribution
  - Top AI models
  - Text length statistics
  - Duplicates removed
  - Invalid rows skipped

## Output Verification

After processing, the script automatically:
1. Verifies all Parquet files are readable
2. Counts total rows across all files
3. Compares with input row count
4. Reports any discrepancies or corrupted files

## Use Cases

### Training AI Detectors

```python
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, Trainer

# Load dataset
dataset = load_dataset('parquet', data_dir='processed_data')

# Balance dataset
human_ds = load_dataset('parquet', data_dir='processed_data/human')
ai_ds = load_dataset('parquet', data_dir='processed_data/ai/gpt4')

# Train model
# ... your training code
```

### Statistical Analysis

```python
import pandas as pd
import json

# Load statistics
with open('processed_data/statistics.json') as f:
    stats = json.load(f)

print(f"Total samples: {stats['total_samples']:,}")
print(f"Human: {stats['human_percentage']:.1f}%")
print(f"AI: {stats['ai_percentage']:.1f}%")
```

### Model-Specific Analysis

```python
# Analyze GPT-4 outputs
df_gpt4 = pd.concat([
    pd.read_parquet(f) 
    for f in Path('processed_data/ai/gpt4').glob('*.parquet')
])

print(f"GPT-4 samples: {len(df_gpt4):,}")
print(f"Average length: {df_gpt4['text_length'].mean():.0f}")
```

## Best Practices

1. **Always validate first**: Run with `--validate-only` to check your dataset
2. **Start small**: Test with a small chunk size first
3. **Monitor memory**: Watch the memory usage warnings
4. **Save checkpoints**: Use appropriate `--checkpoint-interval`
5. **Backup original data**: Keep your original CSV file safe
6. **Check output**: Review the statistics.json and verify output

## License

This project is provided as-is for educational and research purposes.

## Contributing

Feel free to submit issues, feature requests, or improvements.

## Support

For issues or questions:
1. Check this README for solutions
2. Review the processing_log.txt file
3. Run with `--validate-only` to diagnose issues
4. Check available disk space and memory

## Version History

- **v1.0.0** (2025-10-18): Initial release
  - Automatic schema detection
  - Memory-efficient chunk processing
  - Intelligent data segregation
  - Parquet output with compression
  - Real-time analytics and progress tracking
  - Checkpointing and resume capability
  - Validation mode
  - Comprehensive error handling

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Happy Processing! 🚀**
