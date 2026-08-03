---
id: tool-07187
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 本地写作]
title: media_narrative_evolution_analysis
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/chirindaopensource/media_narrative_evolution_analysis
created: 2026-07-18
updated: 2026-07-18
no: 7187
category: 画龙补充 / 扩容入库 — 补充源
repo: chirindaopensource/media_narrative_evolution_analysis
stars: 1
url: https://github.com/chirindaopensource/media_narrative_evolution_analysis
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# chirindaopensource/media_narrative_evolution_analysis

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/chirindaopensource/media_narrative_evolution_analysis
- **Stars**：1
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：computational-social-science, dynamic-topic-models, gensim, huggingface, large-language-models, narrative-analysis, natural-language-processing, numpy, pandas, scikit-learn, spacy, text-mining, topic-modeling
- **GitHub 描述**：A Python implementation of hybrid Dynamic Topic Models and Large Language Models for detecting narrative shifts in longitudinal text corpora. Enables scalable analysis of media discourse evolution with statistical rigor and LLM-powered semantic interpretation.
- **本地描述**：media_narrative_evolution_analysis
- **拉取时间**：2026-07-25 19:13:30

---

# README.md

# Narrative Shift Detection: A Hybrid DTM-LLM Approach 

<!-- PROJECT SHIELDS -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: flake8](https://img.shields.io/badge/linting-flake8-yellowgreen)](https://flake8.pycqa.org/)
[![Type Checking: mypy](https://img.shields.io/badge/type_checking-mypy-blue)](http://mypy-lang.org/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)](https://matplotlib.org/)
[![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=flat&logo=spacy&logoColor=white)](https://spacy.io/)
[![Gensim](https://img.shields.io/badge/Gensim-FF6B35?style=flat&logoColor=white)](https://radimrehurek.com/gensim/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-FFD21E?style=flat&logoColor=black)](https://huggingface.co/)
[![Transformers](https://img.shields.io/badge/Transformers-FF6F00?style=flat&logoColor=white)](https://huggingface.co/transformers/)
[![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat&logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda-toolkit)
[![Jupyter](https://img.shields.io/badge/Jupyter-%23F37626.svg?style=flat&logo=Jupyter&logoColor=white)](https://jupyter.org/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://pytest.org/)
[![JSON Schema](https://img.shields.io/badge/JSON%20Schema-000000?style=flat&logo=json&logoColor=white)](https://json-schema.org/)
[![arXiv](https://img.shields.io/badge/arXiv-b31b1b?style=flat&logo=arxiv&logoColor=white)](https://arxiv.org/)
[![DOI](https://img.shields.io/badge/DOI-10.000%2F000000-blue)](https://doi.org/)
[![Research](https://img.shields.io/badge/Research-Computational%20Social%20Science-green)](https://github.com/)
[![Methodology](https://img.shields.io/badge/Methodology-Hybrid%20DTM--LLM-orange)](https://github.com/)
[![Memory Profiling](https://img.shields.io/badge/Memory-Profiling%20Enabled-red)](https://pypi.org/project/memory-profiler/)
[![GPU Accelerated](https://img.shields.io/badge/GPU-Accelerated-76B900)](https://developer.nvidia.com/cuda-toolkit)
[![Quantization](https://img.shields.io/badge/Model-Quantization%20Support-purple)](https://github.com/TimDettmers/bitsandbytes)
[![Text Processing](https://img.shields.io/badge/Text-Processing-blue)](https://spacy.io/)
[![Topic Modeling](https://img.shields.io/badge/Topic-Modeling-orange)](https://radimrehurek.com/gensim/)
[![Change Detection](https://img.shields.io/badge/Change%20Point-Detection-red)](https://scipy.org/)
[![Statistical Analysis](https://img.shields.io/badge/Statistical-Analysis-green)](https://scipy.org/)
[![Bootstrap Methods](https://img.shields.io/badge/Bootstrap-Resampling-yellow)](https://scipy.org/)


**Repository:** https://github.com/chirindaopensource/media_narrative_evolution_analysis

**Owner:** 2025 Craig Chirinda (Open Source Projects)



This repository contains an **independent** implementation of the research methodology from a 2025 paper which is entitled **"Narrative Shift Detection: A Hybrid Approach of Dynamic Topic Models and Large Language Models"** by:

* Kai-Robin Lange: Department of Statistics, TU Dortmund University, 44221 Dortmund, Germany.
* Tobias Schmidt: Institute of Journalism, TU Dortmund University, 44221 Dortmund, Germany.
* Matthias Reccius: Faculty of Management and Economics, Ruhr University Bochum, 44780 Bochum, Germany.
* Henrik Müller: Institute of Journalism, TU Dortmund University, 44221 Dortmund, Germany.
* Michael Roos: Faculty of Management and Economics, Ruhr University Bochum, 44780 Bochum, Germany.
* Carsten Jentsch: Department of Statistics, TU Dortmund University, 44221 Dortmund, Germany.

The project provides a robust, end-to-end Python pipeline for identifying, analyzing, and understanding the evolution of narratives within large-scale longitudinal text corpora.

## Table of Contents

- [Introduction](#introduction)
- [Theoretical Background](#theoretical-background)
- [Features](#features)
- [Methodology Implemented](#methodology-implemented)
- [Core Components (Notebook Structure)](#core-components-notebook-structure)
- [Key Callable: run_narrative_shift_detection_pipeline](#key-callable-run_narrative_shift_detection_pipeline)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Input Data Structure](#input-data-structure)
- [Usage](#usage)
- [Output Structure](#output-structure)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)

## Introduction

This project provides a Python implementation of the methodologies presented in the 2025 paper "Narrative Shift Detection: A Hybrid Approach of Dynamic Topic Models and Large Language Models." The core of this repository is the iPython Notebook `narrative_shift_detection_draft.ipynb`, which contains a comprehensive suite of functions to analyze narrative evolution in longitudinal text corpora.

Analyzing how media narratives evolve over time is a critical task in computational social science, finance, and political economy. Traditional quantitative methods like topic modeling are scalable but often lack the semantic depth to understand complex narrative structures. Conversely, Large Language Models (LLMs) possess sophisticated language understanding but are computationally prohibitive to apply across entire large-scale corpora for continuous monitoring.

This framework enables researchers to:

- Detect significant narrative shifts in large text corpora
- Identify the temporal moments when narratives change
- Classify changes as "content shifts" or "narrative shifts" using the Narrative Policy Framework (NPF)
- Provide computational efficiency through hybrid DTM-LLM architecture

This codebase is intended for researchers and students in computational social science, journalism, political science, and related fields who require robust tools for quantitative narrative analysis.

## Theoretical Background

The implemented methods are grounded in the theoretical constructs combining Dynamic Topic Models (DTMs) and Large Language Models (LLMs):

**Dynamic Topic Modeling:** Utilizes Latent Dirichlet Allocation (LDA) with temporal coherence to track topic evolution over time. The pipeline implements:
- Stable Topic Initialization to mitigate LDA stochasticity
- Rolling Window LDA for temporal topic tracking
- Statistical change point detection using bootstrap methods

**Narrative Policy Framework (NPF):** Provides the theoretical foundation for classifying narrative changes into:
- Content Shifts: Changes in topic focus or emphasis without fundamental narrative restructuring
- Narrative Shifts: Deeper changes in how stories are framed, including character roles, plot structure, and moral positioning

**Hybrid Architecture:** Combines the scalability of DTMs for corpus-wide analysis with the semantic depth of LLMs for targeted narrative interpretation, achieving both computational efficiency and analytical sophistication.

## Features

The provided iPython Notebook (`narrative_shift_detection_draft.ipynb`) implements a full pipeline for narrative shift detection, including:

- **Input Validation:** Rigorous checks for input data schema, parameter types, and value ranges
- **Text Preprocessing:** Advanced text cleaning, tokenization, and lemmatization using spaCy
- **Stable Topic Initialization:** LDAPrototype algorithm for consistent topic model initialization
- **Dynamic Topic Evolution:** RollingLDA implementation for temporal topic tracking
- **Statistical Change Point Detection:** Bootstrap-based hypothesis testing for significant topic shifts
- **Document Filtering:** Intelligent selection of relevant documents for LLM analysis
- **LLM-based Narrative Analysis:** Structured prompting for narrative shift classification
- **Performance Evaluation:** Comprehensive metrics comparing LLM classifications to human annotations
- **Visualization Suite:** Time series plots, topic evolution charts, and performance summaries
- **Comprehensive Reporting:** Detailed documentation of pipeline runs for reproducibility

## Methodology Implemented

The core analytical steps directly implement the hybrid DTM-LLM methodology:

1. **Stable Topic Initialization**: Mitigates LDA stochasticity by training multiple models on a warm-up corpus and selecting the most stable representative model as a prototype.

2. **Dynamic Topic Evolution**: Models topic evolution using a rolling window approach where topic-word distributions from previous time steps inform current models, ensuring temporal coherence while allowing adaptation.

3. **Statistical Change Point Detection**: Applies bootstrap-based hypothesis testing to time series of topic-word distributions, detecting statistically significant abrupt shifts and identifying key words driving changes.

4. **Document Filtering**: Selects the most relevant documents for each detected change point based on topic relevance scores and temporal proximity.

5. **LLM-based Narrative Analysis**: Uses carefully engineered prompts to instruct an LLM (Llama 3.1 8B) to analyze changes, classify them according to NPF, and provide structured explanations in JSON format.

6. **Performance Evaluation**: Compares LLM classifications against human annotations using standard metrics (accuracy, precision, recall, F1-score).

## Core Components (Notebook Structure)

The `narrative_shift_detection_draft.ipynb` notebook is structured as a logical pipeline with modular functions:

**Input Processing and Validation:**
- `validate_input_parameters`: Ensures all pipeline inputs are correctly structured
- `cleanse_news_data`: Handles missing values and cleans raw text corpus
- `preprocess_text_data`: Performs tokenization, lemmatization, and creates bag-of-words representation
- `chunk_data_by_time`: Partitions corpus into discrete time chunks

**Topic Modeling Pipeline:**
- `train_lda_prototype`: Implements LDAPrototype algorithm for stable base topic model
- `apply_rolling_lda`: Executes RollingLDA model for topic evolution tracking
- `detect_topical_changes`: Implements bootstrap-based statistical test for change point detection

**LLM Analysis Pipeline:**
- `filter_documents_for_llm`: Selects most relevant documents for change point analysis
- `setup_llm_model_and_tokenizer`: Loads and configures specified LLM and tokenizer
- `construct_llm_prompt_for_narrative_analysis`: Engineers detailed structured prompts
- `perform_llm_analysis_on_change_point`: Manages LLM inference and JSON output parsing

**Evaluation and Reporting:**
- `evaluate_llm_classification_performance`: Calculates performance metrics against human labels
- `compile_analysis_results`: Aggregates all system, LLM, and human data
- `plot_topic_evolution_and_changes`: Generates visualizations
- `generate_pipeline_run_documentation`: Creates detailed run reports

**Main Orchestrator:**
- `run_narrative_shift_detection_pipeline`: Executes the entire pipeline in sequence

## Key Callable: run_narrative_shift_detection_pipeline

The central function in this project is `run_narrative_shift_detection_pipeline`. It orchestrates the entire analytical workflow.

```python
def run_narrative_shift_detection_pipeline(
    # Parameters (i) to (vii) from the main problem description
    news_article_data_frame_input: pd.DataFrame,
    lda_prototype_params_input: Dict[str, Any],
    rolling_lda_params_input: Dict[str, Any],
    topical_changes_params_input: Dict[str, Any],
    llm_interpretation_params_input: Dict[str, Any],
    general_study_params_input: Dict[str, Any],
    human_annotations_input_data: Dict[str, Dict[str, Any]],

    # Detailed configuration parameters for individual pipeline steps
    spacy_model_name_cfg: str = "en_core_web_sm",
    custom_stopwords_cfg: Optional[List[str]] = None,
    countvectorizer_min_df_cfg: int = 5,
    countvectorizer_max_df_cfg: float = 0.95,

    lda_iterations_prototype_cfg: int = 1000,
    lda_alpha_prototype_cfg: str = 'symmetric',
    lda_eta_prototype_cfg: Optional[Any] = None, # Gensim default (symmetric based on num_topics if None)
    lda_passes_prototype_cfg: int = 10, # Added for completeness for train_lda_prototype

    rolling_lda_iterations_warmup_cfg: int = 50,
    rolling_lda_iterations_update_cfg: int = 20,
    rolling_lda_passes_warmup_cfg: int = 10,
    rolling_lda_passes_update_cfg: int = 1,
    rolling_lda_alpha_cfg: str = 'symmetric',
    rolling_lda_epsilon_eta_cfg: float = 1e-9,

    tc_num_tokens_bootstrap_cfg: int = 10000,
    tc_num_significant_loo_cfg: int = 10,
    tc_epsilon_cfg: float = 1e-9,

    llm_quantization_cfg: Optional[Dict[str, Any]] = None,
    llm_auth_token_cfg: Optional[str] = None,
    llm_trust_remote_code_cfg: bool = True, # Often needed for newer models
    llm_use_cache_cfg: bool = True, # For setup_llm_model_and_tokenizer cache

    llm_max_new_tokens_cfg: int = 3072,

    eval_topic_matching_threshold_cfg: float = 0.1,
    analysis_num_top_words_display_cfg: int = 5,
    analysis_mapping_num_top_words_cfg: int = 10, # For compile_analysis_results mapping helper

    viz_plots_per_row_cfg: int = 5,
    viz_figure_title_cfg: str = "Topic Evolution and Detected Narrative Shifts",

    output_directory_cfg: Optional[str] = None,

    doc_run_notes_cfg: Optional[List[str]] = None,
    doc_output_format_cfg: str = "json"

) -> Dict[str, Any]:
    """
    Orchestrates the entire end-to-end narrative shift detection pipeline,
    integrating all defined tasks from data validation to documentation.

    This function manages the flow of data between modular components,
    handles configuration, and implements saving of large artifacts to disk
    if an output directory is specified.

    Args:
        news_article_data_frame_input: Raw news articles DataFrame (param i).
        lda_prototype_params_input: Params for LDAPrototype (param ii).
        rolling_lda_params_input: Params for RollingLDA (param iii).
        topical_changes_params_input: Params for Topical Changes (param iv).
        llm_interpretation_params_input: Params for LLM interpretation (param v).
        general_study_params_input: General study parameters (param vi).
        human_annotations_input_data: Pre-existing human annotations (param vii).
        spacy_model_name_cfg: Name of spaCy model for preprocessing.
        custom_stopwords_cfg: Custom stopwords for preprocessing.
        countvectorizer_min_df_cfg: Min document frequency for CountVectorizer.
        countvectorizer_max_df_cfg: Max document frequency for CountVectorizer.
        lda_iterations_prototype_cfg: Iterations for LDA in LDAPrototype.
        lda_alpha_prototype_cfg: Alpha for LDA in LDAPrototype.
        lda_eta_prototype_cfg: Eta for LDA in LDAPrototype.
        lda_passes_prototype_cfg: Passes for LDA in LDAPrototype.
        rolling_lda_iterations_warmup_cfg: Iterations for RollingLDA warm-up.
        rolling_lda_iterations_update_cfg: Iterations for RollingLDA updates.
        rolling_lda_passes_warmup_cfg: Passes for RollingLDA warm-up.
        rolling_lda_passes_update_cfg: Passes for RollingLDA updates.
        rolling_lda_alpha_cfg: Alpha for RollingLDA.
        rolling_lda_epsilon_eta_cfg: Epsilon for RollingLDA eta.
        tc_num_tokens_bootstrap_cfg: N tokens for Topical Changes bootstrap.
        tc_num_significant_loo_cfg: N LOO words for Topical Changes.
        tc_epsilon_cfg: Epsilon for Topical Changes numerical stability.
        llm_quantization_cfg: Quantization config for LLM setup.
        llm_auth_token_cfg: Auth token for LLM setup.
        llm_trust_remote_code_cfg: Trust remote code for LLM.
        llm_use_cache_cfg: Whether to use internal cache in LLM setup.
        llm_max_new_tokens_cfg: Max new tokens for LLM generation.
        eval_topic_matching_threshold_cfg: Threshold for mapping system to human topics.
        analysis_num_top_words_display_cfg: Num top words for topic display in analysis DF.
        analysis_mapping_num_top_words_cfg: Num top words for topic matching in analysis mapping.
        viz_plots_per_row_cfg: Plots per row in topic evolution visualization.
        viz_figure_title_cfg: Title for the topic evolution figure.
        output_directory_cfg (Optional[str]): Base directory to save all generated
                                             artifacts. If None, artifacts are not saved.
        doc_run_notes_cfg (Optional[List[str]]): User notes for the documentation.
        doc_output_format_cfg (str): Format for run documentation ('json' or 'markdown').

    Returns:
        Dict[str, Any]: A comprehensive dictionary containing key outputs from each major
                        step of the pipeline. If `output_directory_cfg` is provided,
                        this dictionary will contain paths to saved artifacts.
    """
    # ... (implementation)
```

This function takes the raw data and configuration parameters, performs all analytical steps, and returns a comprehensive results dictionary. Refer to its docstring in the notebook for detailed parameter descriptions.

## Prerequisites

**Python Requirements:**
- Python 3.9 or higher (required for advanced typing features and library compatibility)

**Core Dependencies:**
- pandas: For data manipulation and DataFrame structures
- numpy: For numerical operations and array manipulations
- scipy: For statistical computations and bootstrap methods
- scikit-learn: For machine learning utilities and metrics
- matplotlib: For visualization and plotting
- spacy: For natural language processing and text preprocessing
- gensim: For topic modeling (LDA implementation)
- torch: For PyTorch-based LLM operations
- transformers: For Hugging Face model integration

**Additional Requirements:**
- CUDA-enabled GPU with ≥16GB VRAM (recommended for LLM inference)
- Hugging Face Hub authentication for model access

**Installation:**
```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
huggingface-cli login  # For model access
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/chirindaopensource/media_narrative_evolution_analysis.git
   cd media_narrative_evolution_analysis
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Download spaCy model:**
   ```sh
   python -m spacy download en_core_web_sm
   ```

4. **Configure LLM access:**
   ```sh
   huggingface-cli login
   ```

## Data Structure

The primary data input for the `run_narrative_shift_detection_pipeline` function is a pandas DataFrame with specific structure:

**Type:** `pd.DataFrame`
**Required Structure:**
- **Index:** DatetimeIndex representing publication dates
- **Columns:** Text columns containing news articles or documents
- **Data Types:** String values for text content, datetime index for temporal analysis

**Example DataFrame structure:**
```python
    mock_corpus_data = [
        # --- Pre-shift period (2021) ---
        {'article_id': 'A001', 'date': '2021-01-15', 'headline': 'Market Hits New High', 'full_text': 'The stock market reached a new peak today driven by strong financial sector performance.'},
        {'article_id': 'A002', 'date': '2021-02-20', 'headline': 'Tech Innovations Drive Growth', 'full_text': 'New technology and software innovation are pushing the economy forward. The future of tech is bright.'},
        {'article_id': 'A003', 'date': '2021-03-10', 'headline': 'Federal Reserve Policy', 'full_text': 'The federal reserve announced its new policy on interest rates, affecting the financial market.'},
        {'article_id': 'A004', 'date': '2021-04-05', 'headline': 'Startup Ecosystem Thrives', 'full_text': 'The technology startup ecosystem sees record investment and innovation.'},
        # ... Add more articles to ensure sufficient data for the 12-month warm-up ...
        {'article_id': 'A005', 'date': '2021-05-15', 'headline': 'Quarterly Earnings Report', 'full_text': 'Major banks report strong quarterly earnings, boosting the market.'},
        {'article_id': 'A006', 'date': '2021-06-20', 'headline': 'AI in Software Development', 'full_text': 'Artificial intelligence is a key technology for modern software.'},
        {'article_id': 'A007', 'date': '2021-07-10', 'headline': 'Inflation Concerns Rise', 'full_text': 'Economists express concern over rising inflation and its impact on the market.'},
        {'article_id': 'A008', 'date': '2021-08-05', 'headline': 'Cloud Computing Expands', 'full_text': 'The cloud computing technology sector continues its rapid expansion.'},
        {'article_id': 'A009', 'date': '2021-09-15', 'headline': 'Bond Market Reacts', 'full_text': 'The bond market reacts to new financial data.'},
        {'article_id': 'A010', 'date': '2021-10-20', 'headline': 'Next-Gen Tech Unveiled', 'full_text': 'A major technology firm unveils its next-generation hardware and software.'},
        {'article_id': 'A011', 'date': '2021-11-10', 'headline': 'Global Trade Update', 'full_text': 'An update on global trade agreements and their effect on the financial market.'},
        {'article_id': 'A012', 'date': '2021-12-05', 'headline': 'Year-End Tech Review', 'full_text': 'A review of the year in technology highlights major software and hardware achievements.'},
        {'article_id': 'A013', 'date': '2022-01-15', 'headline': 'Market Opens Strong', 'full_text': 'The financial market opens the year with strong gains.'},
        {'article_id': 'A014', 'date': '2022-02-20', 'headline': 'Software as a Service Grows', 'full_text': 'The software as a service technology model continues to show robust growth.'},

        # --- Post-shift period (March 2022 onwards) ---
        # The narrative around 'technology' now includes 'crisis', 'regulation', 'layoffs'.
        {'article_id': 'A015', 'date': '2022-03-10', 'headline': 'Tech Bubble Concerns', 'full_text': 'Concerns of a technology bubble lead to a market crisis. Regulation is now being discussed.'},
        {'article_id': 'A016', 'date': '2022-03-15', 'headline': 'Layoffs Hit Tech Sector', 'full_text': 'Major technology firms announce widespread layoffs amid the economic crisis. The software industry faces new regulation.'},
        {'article_id': 'A017', 'date': '2022-04-05', 'headline': 'Financial Markets Tumble', 'full_text': 'Financial markets tumble as the technology sector crisis deepens. Investors are worried.'},
        {'article_id': 'A018', 'date': '2022-04-20', 'headline': 'Government Scrutinizes Tech', 'full_text': 'The government begins to scrutinize big technology companies, proposing new regulation following the recent crisis and layoffs.'},
    ]
    # Create the pandas DataFrame from the mock data.
    news_article_data_frame_input = pd.DataFrame(mock_corpus_data)
    # Convert the 'date' column to datetime objects.
    news_article_data_frame_input['date'] = pd.to_datetime(news_article_data_frame_input['date'])
    # Set the 'date' column as the DataFrame's index, which is required by the pipeline.
    news_article_data_frame_input = news_article_data_frame_input.set_index('date')
    print("Mock DataFrame created successfully.")
```

**Configuration Parameters:**
- `lda_prototype_params`: LDA model parameters (K_topics, N_lda_runs)
- `rolling_lda_params`: Rolling window parameters (w_warmup, m_memory, K_topics)
- `topical_changes_params`: Change detection parameters (z_lookback, alpha_significance, B_bootstrap)
- `llm_interpretation_params`: LLM configuration (model_name, temperature, N_docs_filter)
- `general_study_params`: Study parameters (time_chunk_granularity, corpus_start_date, corpus_end_date)
- `human_annotations_input_data`: Ground truth annotations for evaluation

## Usage

**Open and Run the Notebook:**
1. Open `narrative_shift_detection_draft.ipynb` in Jupyter Notebook or JupyterLab
2. Execute cells in order to define all functions and dependencies
3. Examine the usage example in the notebook

**Execute the Pipeline:**
```python
# Usage Example for reference
# Assume all functions from the iPython notebook are defined and available in the scope, 
# Assume all the required Python modules have been imported.
# This example will call `run_narrative_shift_detection_pipeline`.
# from narrative_shift_detection_draft import run_narrative_shift_detection_pipeline

def demonstrate_pipeline_execution() -> None:
    """
    Provides a complete, runnable example of how to set up and execute the
    narrative shift detection pipeline.

    This function meticulously constructs all necessary input data structures and
    configuration dictionaries, then invokes the main pipeline orchestrator.
    It serves as a practical, implementation-grade blueprint for users of the
    pipeline, demonstrating the precise format and structure required for each
    input parameter.

    The example uses a small, synthetic news corpus designed to have a plausible
    narrative shift, allowing the pipeline to be tested end-to-end. It also
    includes a mock human annotation to enable the evaluation stage.

    Note:
        This function assumes that the `run_narrative_shift_detection_pipeline`
        and all its helper functions are defined and available in the current
        Python environment. It also assumes that the required LLM (e.g.,
        "meta-llama/Meta-Llama-3.1-8B-Instruct") is accessible, which may
        require authentication and appropriate hardware (GPU). For this
        demonstration, the LLM-dependent steps will be executed but may be
        slow or require significant resources.
    """
    # --- Step 1: Define All Input Data Structures ---
    # This section creates mock data that is structurally identical to the
    # real-world data the pipeline is designed to process.

    # Sub-step 1.a: Create a mock news article DataFrame (Parameter i)
    # This DataFrame simulates a corpus with a narrative shift around a specific topic.
    # The topic of 'technology' is stable until early 2022, after which it
    # shifts to include terms related to 'crisis' and 'regulation'.
    print("Step 1.a: Constructing mock news article DataFrame...")
    mock_corpus_data = [
        # --- Pre-shift period (2021) ---
        {'article_id': 'A001', 'date': '2021-01-15', 'headline': 'Market Hits New High', 'full_text': 'The stock market reached a new peak today driven by strong financial sector performance.'},
        {'article_id': 'A002', 'date': '2021-02-20', 'headline': 'Tech Innovations Drive Growth', 'full_text': 'New technology and software innovation are pushing the economy forward. The future of tech is bright.'},
        {'article_id': 'A003', 'date': '2021-03-10', 'headline': 'Federal Reserve Policy', 'full_text': 'The federal reserve announced its new policy on interest rates, affecting the financial market.'},
        {'article_id': 'A004', 'date': '2021-04-05', 'headline': 'Startup Ecosystem Thrives', 'full_text': 'The technology startup ecosystem sees record investment and innovation.'},
        # ... Add more articles to ensure sufficient data for the 12-month warm-up ...
        {'article_id': 'A005', 'date': '2021-05-15', 'headline': 'Quarterly Earnings Report', 'full_text': 'Major banks report strong quarterly earnings, boosting the market.'},
        {'article_id': 'A006', 'date': '2021-06-20', 'headline': 'AI in Software Development', 'full_text': 'Artificial intelligence is a key technology for modern software.'},
        {'article_id': 'A007', 'date': '2021-07-10', 'headline': 'Inflation Concerns Rise', 'full_text': 'Economists express concern over rising inflation and its impact on the market.'},
        {'article_id': 'A008', 'date': '2021-08-05', 'headline': 'Cloud Computing Expands', 'full_text': 'The cloud computing technology sector continues its rapid expansion.'},
        {'article_id': 'A009', 'date': '2021-09-15', 'headline': 'Bond Market Reacts', 'full_text': 'The bond market reacts to new financial data.'},
        {'article_id': 'A010', 'date': '2021-10-20', 'headline': 'Next-Gen Tech Unveiled', 'full_text': 'A major technology firm unveils its next-generation hardware and software.'},
        {'article_id': 'A011', 'date': '2021-11-10', 'headline': 'Global Trade Update', 'full_text': 'An update on global trade agreements and their effect on the financial market.'},
        {'article_id': 'A012', 'date': '2021-12-05', 'headline': 'Year-End Tech Review', 'full_text': 'A review of the year in technology highlights major software and hardware achievements.'},
        {'article_id': 'A013', 'date': '2022-01-15', 'headline': 'Market Opens Strong', 'full_text': 'The financial market opens the year with strong gains.'},
        {'article_id': 'A014', 'date': '2022-02-20', 'headline': 'Software as a Service Grows', 'full_text': 'The software as a service technology model continues to show robust growth.'},

        # --- Post-shift period (March 2022 onwards) ---
        # The narrative around 'technology' now includes 'crisis', 'regulation', 'layoffs'.
        {'article_id': 'A015', 'date': '2022-03-10', 'headline': 'Tech Bubble Concerns', 'full_text': 'Concerns of a technology bubble lead to a market crisis. Regulation is now being discussed.'},
        {'article_id': 'A016', 'date': '2022-03-15', 'headline': 'Layoffs Hit Tech Sector', 'full_text': 'Major technology firms announce widespread layoffs amid the economic crisis. The software industry faces new regulation.'},
        {'article_id': 'A017', 'date': '2022-04-05', 'headline': 'Financial Markets Tumble', 'full_text': 'Financial markets tumble as the technology sector crisis deepens. Investors are worried.'},
        {'article_id': 'A018', 'date': '2022-04-20', 'headline': 'Government Scrutinizes Tech', 'full_text': 'The government begins to scrutinize big technology companies, proposing new regulation following the recent crisis and layoffs.'},
    ]
    # Create the pandas DataFrame from the mock data.
    news_article_data_frame_input = pd.DataFrame(mock_corpus_data)
    # Convert the 'date' column to datetime objects.
    news_article_data_frame_input['date'] = pd.to_datetime(news_article_data_frame_input['date'])
    # Set the 'date' column as the DataFrame's index, which is required by the pipeline.
    news_article_data_frame_input = news_article_data_frame_input.set_index('date')
    print("Mock DataFrame created successfully.")

    # Sub-step 1.b: Define parameter dictionaries (Parameters ii-vi)
    # These dictionaries configure the core algorithms of the pipeline.
    # The values are taken directly from the paper's specified configuration.
    print("Step 1.b: Defining algorithm parameter dictionaries...")
    # Parameters for LDAPrototype Selection.
    lda_prototype_params_input = {"K_topics": 2, "N_lda_runs": 3} # Reduced for speed in example
    # Parameters for RollingLDA Application.
    rolling_lda_params_input = {"w_warmup": 12, "m_memory": 4, "K_topics": 2} # K_topics must match
    # Parameters for Topical Change Detection.
    topical_changes_params_input = {"z_lookback": 2, "mixture_param_gamma": 0.95, "alpha_significance": 0.01, "B_bootstrap": 100} # Reduced for speed
    # Parameters for LLM-based Narrative Interpretation.
    llm_interpretation_params_input = {"llm_model_name": "meta-llama/Meta-Llama-3.1-8B-Instruct", "llm_temperature": 0.0, "N_docs_filter": 2}
    # General Study Parameters.
    general_study_params_input = {"time_chunk_granularity": "monthly", "corpus_start_date": "2021-01-01", "corpus_end_date": "2022-12-31"}
    print("Parameter dictionaries defined.")

    # Sub-step 1.c: Create mock human-annotated change points (Parameter vii)
    # This dictionary represents the ground truth against which the LLM's
    # classification performance will be evaluated.
    print("Step 1.c: Constructing mock human annotation data...")
    human_annotations_input_data = {
        "2022-03-15": {
            "change_type": "narrative shift",
            "topics": ["technology", "crisis", "regulation", "layoffs"],
            "setting": ["Global technology sector", "Financial markets"],
            "characters": ["Technology companies", "Investors", "Government regulators"],
            "plot": "A previously booming technology sector faces an abrupt crisis, leading to layoffs and prompting calls for government regulation.",
            "moral": "The moral is that unchecked growth in the technology sector is unsustainable and poses systemic risks, necessitating oversight."
        }
        # ... Add more annotations...
    }
    print("Mock human annotations created.")

    # --- Step 2: Define Detailed Pipeline Step Configurations ---
    # These are the more granular settings passed to the orchestrator function.
    print("\nStep 2: Defining detailed pipeline configurations...")
    # Create a temporary directory for pipeline artifacts. This is a robust
    # practice for examples as it ensures cleanup after execution.
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set the output directory configuration to the created temporary directory.
        output_directory_cfg = temp_dir
        print(f"Pipeline artifacts will be saved to temporary directory: {output_directory_cfg}")

        # --- Step 3: Execute the Pipeline ---
        # This is the primary call to the main orchestrator function.
        print("\nStep 3: Executing the narrative shift detection pipeline...")
        # The `run_narrative_shift_detection_pipeline` function is assumed to be
        # imported or defined in the current scope.
        pipeline_outputs = run_narrative_shift_detection_pipeline(
            # Pass all the defined input data structures (Parameters i-vii).
            news_article_data_frame_input=news_article_data_frame_input,
            lda_prototype_params_input=lda_prototype_params_input,
            rolling_lda_params_input=rolling_lda_params_input,
            topical_changes_params_input=topical_changes_params_input,
            llm_interpretation_params_input=llm_interpretation_params_input,
            general_study_params_input=general_study_params_input,
            human_annotations_input_data=human_annotations_input_data,

            # Pass all the detailed configuration settings.
            spacy_model_name_cfg="en_core_web_sm",
            countvectorizer_min_df_cfg=1, # Lowered for small mock corpus
            countvectorizer_max_df_cfg=0.95,
            lda_iterations_prototype_cfg=200, # Reduced for speed
            rolling_lda_iterations_warmup_cfg=100, # Reduced for speed
            rolling_lda_iterations_update_cfg=50, # Reduced for speed
            llm_quantization_cfg={"load_in_8bit": True}, # Use 8-bit quantization to reduce memory
            llm_max_new_tokens_cfg=1024, # Sufficient for the expected JSON output
            output_directory_cfg=output_directory_cfg,
            doc_output_format_cfg="markdown"
        )
        print("Pipeline execution finished.")

        # --- Step 4: Process and Display Pipeline Outputs ---
        # This section demonstrates how to interpret the results returned by the pipeline.
        print("\n--- Pipeline Execution Summary ---")
        # Check the final status of the pipeline run.
        pipeline_status = pipeline_outputs.get("pipeline_status", "Unknown")
        print(f"Final Pipeline Status: {pipeline_status}")

        # If the pipeline failed, print the error message.
        if pipeline_status == "Failed":
            print(f"Error Message: {pipeline_outputs.get('error_message')}")
            print("--- Error Traceback ---")
            print(pipeline_outputs.get('error_traceback'))
        else:
            # If the pipeline succeeded, print a summary of the key outputs.
            # Use json.dumps for a clean, readable printout of the results dictionary.
            # We create a copy to remove potentially large objects before printing.
            summary_outputs = pipeline_outputs.copy()
            # Remove keys that might contain very large data for a cleaner summary print.
            summary_outputs.pop("parameters_and_configurations", None)
            summary_outputs.pop("compiled_analysis_dataframe_path", None)

            print("\n--- Key Pipeline Outputs ---")
            # Pretty-print the summary dictionary.
            print(json.dumps(summary_outputs, indent=2))

            # Load and display the head of the final compiled analysis DataFrame if it was created.
            analysis_df_path = pipeline_outputs.get("compiled_analysis_dataframe_path")
            if analysis_df_path and os.path.exists(analysis_df_path):
                print("\n--- Compiled Analysis DataFrame (Head) ---")
                # Read the saved CSV file into a pandas DataFrame.
                results_df = pd.read_csv(analysis_df_path)
                # Print the first few rows of the DataFrame.
                print(results_df.head().to_string())

            # Display the content of the generated documentation file.
            doc_path = pipeline_outputs.get("documentation_file_path")
            if doc_path and os.path.exists(doc_path):
                print(f"\n--- Generated Run Documentation (from {doc_path}) related:
  - methods/QUICK_START.md
---")
                # Open and read the content of the documentation file.
                with open(doc_path, 'r', encoding='utf-8') as f:
                    # Print the documentation content.
                    print(f.read())

if __name__ == '__main__':
    demonstrate_pipeline_execution()
    print("Demonstration function `demonstrate_pipeline_execution` is defined.")
    print("To run the example, uncomment the call in the `if __name__ == '__main__':` block.")
    print("Ensure all dependencies are installed and you have access to the required LLM and hardware.")
```

**Adapt for Real Data:**
- Replace synthetic data with your own corpus following the input structure requirements
- Adjust parameters based on your corpus characteristics and research questions
- Ensure sufficient computational resources for LLM inference
- Review data quality reports in the output for validation

## Output Structure

The `run_narrative_shift_detection_pipeline` function returns a comprehensive dictionary containing:

**Core Results:**
- `change_points_detected`: List of detected narrative shift points with timestamps and metadata
- `llm_classifications`: Structured classifications of each change point (content vs. narrative shift)
- `topic_evolution_data`: Time series data of topic distributions and evolution
- `performance_metrics`: Evaluation results comparing LLM output to human annotations

**Artifacts and Outputs:**
- `compiled_analysis_dataframe_path`: Path to comprehensive results DataFrame
- `visualizations_directory`: Directory containing generated plots and charts
- `model_artifacts_directory`: Saved topic models and intermediate results
- `pipeline_documentation_path`: Detailed run documentation for reproducibility

**Metadata:**
- `pipeline_execution_time`: Total runtime and performance metrics
- `computational_resources_used`: GPU/CPU usage statistics
- `data_quality_report`: Preprocessing and validation results
- `parameter_configurations`: Complete record of all input parameters

This comprehensive output enables detailed analysis of results, performance evaluation, and reproducible research workflows.

## Project Structure

```
media_narrative_evolution_analysis/
│
├── narrative_shift_detection_draft.ipynb # Main implementation notebook
├── requirements.txt                       # Python package dependencies
├── LICENSE                               # MIT license file
├── README.md                             # This documentation file

```

## Customization

The pipeline offers extensive customization through several key parameters:

**Topic Modeling Customization:**
- `K_topics`: Number of topics for LDA models
- `N_lda_runs`: Number of LDA runs for prototype selection
- `w_warmup`: Warm-up window size for rolling LDA
- `m_memory`: Memory parameter for temporal coherence

**Change Detection Customization:**
- `alpha_significance`: Significance level for statistical tests
- `B_bootstrap`: Number of bootstrap samples
- `z_lookback`: Lookback window for change detection

**LLM Analysis Customization:**
- `llm_model_name`: Choice of LLM model (supports various Hugging Face models)
- `llm_temperature`: Temperature parameter for LLM generation
- `N_docs_filter`: Number of documents to analyze per change point

**Temporal Analysis Customization:**
- `time_chunk_granularity`: Temporal resolution (daily, weekly, monthly)
- `corpus_start_date` / `corpus_end_date`: Analysis time period

Users can modify these parameters to adapt the pipeline to different corpora, research questions, and computational constraints.

## Contributing

Contributions to this project are welcome and greatly appreciated. Please follow these guidelines:

1. **Fork the Repository:** Create your own fork of the project
2. **Create a Feature Branch:** `git checkout -b feature/AmazingFeature`
3. **Code Standards:** 
   - Follow PEP-8 style guidelines
   - Include comprehensive type hints and docstrings
   - Ensure code is compatible with Python 3.9+
4. **Testing:** Write unit tests for new functionality
5. **Documentation:** Update documentation for any new features or changes
6. **Commit Changes:** `git commit -m 'Add some AmazingFeature'`
7. **Push to Branch:** `git push origin feature/AmazingFeature`
8. **Open Pull Request:** Submit a pull request with clear description of changes

**Development Setup:**
```sh
# Install development dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/

# Run linting
flake8 .
black .
isort .
mypy .
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

**MIT License**

Copyright © 2025 Craig Chirinda (Open Source Projects)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Citation

If you use this code or the methodology in your research, please cite the original paper:

```bibtex
@inproceedings{lange2025narrative,
  title={Narrative Shift Detection: A Hybrid Approach of Dynamic Topic Models and Large Language Models},
  author={Lange, Kai-Robin and Schmidt, Tobias and Reccius, Matthias and Müller, Henrik and Roos, Michael and Jentsch, Carsten},
  booktitle={Proceedings of the Text2Story'25 Workshop},
  year={2025},
  address={Luca, Italy},
  month={April}
}
```

**For the Implementation:**
Consider also acknowledging this GitHub repository if the implementation itself was significantly helpful to your research:

```
Chirinda, C. (2025). Narrative Shift Detection: A Hybrid DTM-LLM Approach - Python Implementation. 
GitHub repository: https://github.com/chirindaopensource/media_narrative_evolution_analysis
```

## Acknowledgments

- Special thanks to the authors of the original paper for their groundbreaking research in hybrid narrative analysis methodologies
- Gratitude to the open-source community for the foundational libraries that make this research possible

--

*This README was generated based on the structure and content of `narrative_shift_detection_draft.ipynb` and follows best practices for research software documentation.*
