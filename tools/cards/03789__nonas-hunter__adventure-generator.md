---
id: tool-03789
type: tool
area: 库
status: active
tags: [互动叙事, 文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: adventure-generator
summary: 互动叙事/聊天写故事
source: https://github.com/nonas-hunter/adventure-generator
created: 2026-07-18
updated: 2026-07-18
no: 3789
category: 十七、AI Dungeon 类 / 互动叙事 / 聊天 Bot 库
repo: nonas-hunter/adventure-generator
stars: 3
url: https://github.com/nonas-hunter/adventure-generator
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 15593f2f28f23995
  - methods/网文写作最强SOP.md
---

# nonas-hunter/adventure-generator

- **分类**：十七、AI Dungeon 类 / 互动叙事 / 聊天 Bot 库
- **链接**：https://github.com/nonas-hunter/adventure-generator
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：adventure-stories, ai-dungeons, language-model
- **GitHub 描述**：An exploration into AI generated choose your own adventure stories
- **本地描述**：An exploration into AI generated choose your own adventure stories
- **拉取时间**：2026-07-23 23:59:02

related:
  - methods/网文写作最强SOP.md
---

# The Dungeons
### Luke Nonas-Hunter
An exploration into AI-generated choose your own adventure stories. This project is heavily inspired by [AI Dungeons](https://play.aidungeon.io), an AI based choose your own adventure game created by Latitude. The goal of this project is to build off of the gameplay in AI Dungeons and add other features such as inventory, health, and narrative consistency.

## Running the Code
To run the code you will need the following packages:

- [pytorch](https://pytorch.org/get-started/locally/)
- [spacey](https://spacy.io/usage)
- [numpy](https://numpy.org/install/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

Clicking any of the names above will bring you to the relavent instrucitions to install the package for your given platform.

Currently there is no offical dataset or model parameters for the game however, you can make your own! Create a `.csv` file in the `data` folder with two columns, `source` and `target`. This file will contain your dataset. In the source column place all the prompts you expect to feed your network. In the target column, write out the outputs you expect from the model. These columns should be written in standard english, no fancy formatting needed! Feel free to include punctuation as well. To train a new model open the `training.py` file and scroll to the very bottom. There should be a line of code inside an `if` statement which instantiates a new `training` object. Replace the current parameters used to instantiate the model with the name of the new `.csv` file you've made and a new name you'd like to call your model. An example is shown bellow:
```python
if __name__ == "__main__":
    training = Training("MY_DATA.csv", "MY_MODEL")
```
Once you've filled out that line, run the training.py file and your new model will appear in the `model` folder!

To run the model open the `adventures.py` file and replace the parameters used to instantiate the model in line 22 with the new parameters you just made. An example is shown bellow:
```python
self._model = Model("MY_MODEL", "MY_DATA.csv")
```
Then feel free to replace the current prompt used to start the conversation and you're ready to go! The prompt can be found in the last line of the file (line 55). An example of how this should be done is shown bellow:
```python
game.run("This is my new prompt!")
```
To run the program, in a terminal run the adventures.py file and you'll begin having a conversation with your language model!!!

## The Architecture
The architecture for this project is losely based off of an MVC architecture. A model class keeps track of game state. It updates the game state using a transformer based recurrent neural network to generate text given the previous game state. The neural network is contained in a separate class to make it easier to alter the text generation without affecting the rest of the game. The other two classes, view and controller, are very simple. The view class prints text to the terminal while the controller prompts the user to input text into the terminal. The reason these classes are kept seperate despite their simplicity is that they will most likely represent two different components in the final version of the game which will hopefully be hosted on the website. A simple class structure is defined bellow.

```text
└── Adventure                                       [Main class]
    └── View                                        [Displays game to user]
    └── Controller                                  [Gather input from user]
    └── Model                                       [Keeps track of game state]
        └── Transformer                             [Pytorch transformer language model]
            └── Generator                           [Standard linear layer + softmax to generate output]
            └── Embeddings                          [Embed text as vector]
                └── PositionalEncoding              [Encode position data in input vector]
            └── Encoder                             [Stack of encoder layers]
                └── EncoderLayer                    [A single encoder layer]
                    └── SublayerConnection          [Intermidate connection before a LayerNorm]
                        └── LayerNorm               [A normilization layer]
                    └── MultiHeadedAttention        [Contains multiple attention functions]
                    └── PositionwiseFeedForward     [Feed forward network]
                └── LayerNorm                       [A normilization layer]
            └── Decoder                             [Stack of decoder layers]
                └── DecoderLayer                    [A single decoder layer]
                    └── SublayerConnection          [Intermidate connection before a LayerNorm]
                        └── LayerNorm               [A normilization layer]
                    └── MultiHeadedAttention        [Contains multiple attention functions]
                    └── PositionwiseFeedForward     [Feed forward network]
                └── LayerNorm                       [A normilization layer]
        └── Training                                [Train the language model]
            └── Batch                               [Holds batches of source and target data for training]
            └── NoamOpt                             [Optim wrapper that implements changing rate]
            └── LabelSmoothing                      [Reduce model's confidence]
            └── SimpleLossCompute                   [Calculate incorrectness of model for training]
            └── AdventureCollate                    [Restructure batches for use in training]
            └── AdventureDataset                    [Load training and vocab data from csv]
                └── Vocabulary                      [Hold model vocabulary]
```
