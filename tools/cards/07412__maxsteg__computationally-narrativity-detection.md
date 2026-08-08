---
id: tool-07412
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: computationally-narrativity-detection
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/maxsteg/computationally-narrativity-detection
created: 2026-07-18
updated: 2026-07-18
no: 7412
category: 画龙补充 / 扩容入库 — 补充源
repo: maxsteg/computationally-narrativity-detection
stars: 0
url: https://github.com/maxsteg/computationally-narrativity-detection
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: dadd1b058a1ff27a
  - methods/QUICK_START.md
---

# maxsteg/computationally-narrativity-detection

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/maxsteg/computationally-narrativity-detection
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：computationally-narrativity-detection
- **拉取时间**：2026-07-25 19:21:06

---

---------------------------------
READ ME
---------------------------------

This document explains what code can be found in this directory and how to use it.
Special thanks to Piper et al. (2021) for the foundation of this code.

The original code can be found here: https://doi.org/10.7910/DVN/DAWVME
The accompanying paper can be found here: http://ceur-ws.org/Vol-2989/long_paper49.pdf


IMPORTANT: To prevent problems running parts of the code, edit the variable BOOK_PATH in /src/classifier/config.py to
the absolute path of the BookNLP output on your PC. The data set, BookNLP output and Concreteness Rating files are not standard included in this project
directory.

---------------------------------
FILES AND HOW TO USE
------------------------------related:
  - methods/QUICK_START.md
---

##### SUBDIRECTORY dataset

BookNLP_output - this directory contains the BookNLP output for all annotated files (Piper et al., 2022). It is being used in our models to calculate the values of our features.

minNarrative_txtfiles - this directory contains the textfiles for the complete data set (17+ documents)

Dataset\_and\_BookNLP_processing.ipynb - This notebook takes the complete dataset as input and removes all non-annotated files. The annotated files are processed by BookNLP. We used Google Colab to run this notebook (due to computational limitations). The output of this code can be found in BookNLP\_output

MinNarrative\_ReaderData_Final.csv - Annotated data set from Piper et al. (2022). A part of their computed feature values are included in this file and used by our model during training.

Steg\_Extended\_MinNarrative\_ReaderData\_Final.csv  - Annotated data set from Piper et al. (2022). A part of their computed feature values are included in this file and used by our model during training. Our computed feature values are included in this file as well.

Concreteness\_ratings\_Brysbaert\_et\_al_BRM - Concreteness ratings Brysbaert et al. for 1- and 2-word expressions

MultiwordExpression\_Concreteness\_Ratings.csv - Concreteness ratings Muraki et al. for multiword expressions.


#### SUBDIRECTORY src/classifier

doc2vec - This directory contains our pretrained Doc2Vec model trained on the complete dataset (17+ documents)

lda - This directory contains our pretrained LDA model trained on the complete dataset (17+ documents)

results - This directory contains the results of our experiments. It contains files for 2- and 3-class experiments, the baselines, individual features and combinations of features.

doc2vec.py - Used to train a Doc2Vec model and save it, so it can be used by our models.

lda.py - Used to train a LDA model and save it, so it can be used by our models.

main.py - Used to train and test our models. Can be run with the command 'python3 main.py'. At the
end of the file can be specified which algorithm has to be used, the number of folds, 2- or 3-class and which features (combinations) you want to train and test models for. The output is saved in a file in the directory 'results'
To make the code properly work,

tuning.py, vectorizer.py, config.py, data_loader.py - These files are being used by main.py and other notebooks to obtain the vectors and feature values, train and test the model, load the data, and define global variables.

analysis.ipynb - Jupyter Notebook needs to be run from the directory 'src/classifier' to make this notebook work. This notebook is used to analyse our best model (SVM 2-class, TfIDF). The notebook calcultates the degree of narrativity for all files in our dataset (17k+), calculates the average degree of narrativity for each genre and is able to analyse which words play an important role in predicting the degree of narrativity.

interpretation.ipynb - Jupyter Notebook needs to be run from the directory 'src/classifier' to make this notebook work. This notebook is used to calculate and plot correlation between our feature values and the annotation scores for the annotated passages. The notebook also calculates correlation between individual features.

