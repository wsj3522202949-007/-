---
id: tool-07189
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 中文友好, 本地写作]
title: sbd
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/cicistar/sbd
created: 2026-07-18
updated: 2026-07-18
no: 7189
category: 画龙补充 / 扩容入库 — 补充源
repo: cicistar/sbd
stars: 0
url: https://github.com/cicistar/sbd
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 59b1c81643c3fe3b
  - methods/QUICK_START.md
---

# cicistar/sbd

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/cicistar/sbd
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Sentences boundary detection for ancient Chinese texts
- **本地描述**：sbd
- **拉取时间**：2026-07-25 19:13:33

related:
  - methods/QUICK_START.md
---

# 古文句读
由于使用刀具刻版非常困难等原因，古人并未习惯于使用标点或断句符号。现存的几乎所有的古文篇章依然缺少标点。在阅读古文时需要根据自己的知识和经验自行断句。所以古代的启蒙教育十分重视句读能力。《礼记·学记》中的“一年视离经辨志”说的就是句读能力训练的重要性。古汉语自动断句及标点是指根据古代汉语句子特点，结合现代汉语当中的标点符号用法，通过计算机自动切割、断开连续的文本字符序列为句（或子句），然后根据需要及规范添加标点。

# 配置
python == 3.6.8
tensorflow-gpu == 1.13.1

# 模型训练
1. 把句子进行如下转换（更多实例参考 sample_test.txt ）：
原句：
```
终必成道。故圣经云：中也者。天下之大本也。和也者，天下之达道也。致中和天地位焉，
```

转换后：
```
终必成道故圣经云中也者天下之大本也和也者天下之达道也致中和天地位焉|[B_.] [I_.] [I_.] [I_.] [B_:] [I_:] [I_:] [I_:] [B_,] [I_,] [I_,] [B_.] [I_.] [I_.] [I_.] [I_.] [I_.] [B_,] [I_,] [I_,] [B_.] [I_.] [I_.] [I_.] [I_.] [I_.] [B_,] [I_,] [I_,] [B_,] [I_,] [I_,] [I_,]
```

2. 获得模型能够处理的数据格式。
```
python to_bert_record.py --task_name=to_tfrecord --data_dir={$SOURCE_PATH} --output_dir={$TF_PATH} --max_seq_length={$MAX_LEN} --vocab_file=./vocab.txt
```		
样例：
```
python to_bert_record.py --task_name=to_tfrecord --data_dir=./sample_text.txt --output_dir=./tfdata/sample.tf_record --max_seq_length=64 --vocab_file=./vocab.txt
```
	
3. 模型训练
```
python BERT_SEG.py  --training_examples={$EXAMPLES} --eval_examples=1 --pred_examples=1 --task_name="SEG" --do_train=True --do_eval=False --do_predict=False --data_dir=./ --vocab_file=./vocab.txt --bert_config_file=./bert_config.json --init_checkpoint={$PRETRAIN_CKPT_PATH} --max_seq_length={$MAX_LEN} --train_batch_size={$BATH_SIZE} --learning_rate=2e-5 --num_train_epochs={$EPOCHS} --output_dir={$SAVE_PATH}
```
样例：
```
python BERT_SEG.py  --training_examples=6 --eval_examples=1 --pred_examples=1 --task_name="SEG" --do_train=True --do_eval=False --do_predict=False --data_dir=./ --vocab_file=./vocab.txt --bert_config_file=./bert_config.json --init_checkpoint=./pretraining_output/model.ckpt-250000 --max_seq_length=64 --train_batch_size=8 --learning_rate=5e-5 --num_train_epochs=5.0 --output_dir=./output
```

# 模型预测
```
python BERT_SEG.py  --training_examples=1 --eval_examples=1 --pred_examples=1 --task_name="SEG" --do_train=False --do_eval=False --do_predict=True --data_dir=./ --vocab_file=./vocab.txt --bert_config_file=./bert_config.json --init_checkpoint={$CKPT_PATH} --max_seq_length={$MAX_LEN} --train_batch_size=128 --learning_rate=2e-5 --num_train_epochs=1.0 --output_dir={$OUTPUT_PATH}
```
样例：
```
python BERT_SEG.py  --training_examples=1 --eval_examples=1 --pred_examples=1 --task_name="SEG" --do_train=False --do_eval=False --do_predict=True --data_dir=./ --vocab_file=./vocab.txt --bert_config_file=./bert_config.json --init_checkpoint=./output/model.ckpt-3 --max_seq_length=64 --train_batch_size=128 --learning_rate=2e-5 --num_train_epochs=1.0 --output_dir=./output
```
		
# 参考
模型实现请参考（If you make use of this software for research purposes, we'll appreciate citing the following）：
```
俞敬松,魏一,张永伟.基于BERT的古文断句研究与应用[J].中文信息学报,2019,33(11):50-56.
```
http://jcip.cipsc.org.cn/CN/abstract/abstract2861.shtml
