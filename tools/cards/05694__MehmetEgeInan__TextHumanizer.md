---
id: tool-05694
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: TextHumanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/mehmetegeinan/texthumanizer
created: 2026-07-18
updated: 2026-07-18
no: 5694
category: 一、去 AI 味 / Humanizer 库
repo: MehmetEgeInan/TextHumanizer
stars: 0
url: https://github.com/mehmetegeinan/texthumanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MehmetEgeInan/TextHumanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mehmetegeinan/texthumanizer
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Offline Turkish Academic Text Humanizer powered by Local LLMs & Docker.
- **本地描述**：Offline Turkish Academic Text Humanizer powered by Local LLMs & Docker.
- **拉取时间**：2026-07-25 18:28:09

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# TextHumanizer
Offline Turkish Academic Text Humanizer powered by Local LLMs & Docker.

🛠️ Kurulum
Bu projeyi çalıştırmak için bilgisayarınızda Docker Desktop yüklü olmalıdır.

1. Repoyu Klonlayın
Bash

git clone https://github.com/KULLANICI_ADINIZ/TezHumanizer.git
cd TezHumanizer
2. Yapay Zeka Modelini İndirin (Çok Önemli!)
Bu repo, boyutları çok büyük olduğu için yapay zeka modelini içermez. Aşağıdaki modellerden birini indirip projedeki models/ klasörünün içine atmalısınız.

Seçenek A (Önerilen - Yüksek Kalite): Meta-Llama-3-8B-Instruct.Q4_K_M.gguf (~5 GB)

Seçenek B (Hız Odaklı - Düşük Sistem): Phi-3-mini-4k-instruct.Q4_K_M.gguf (~2.5 GB)

İndirdiğiniz dosyayı models/ klasörüne taşıyın. Klasör yapınız şöyle görünmelidir:

Plaintext

TezHumanizer/
├── app/
├── models/
│   └── Meta-Llama-3-8B-Instruct.Q4_K_M.gguf
├── docker-compose.yml
├── Dockerfile
└── README.md
3. Sistemi Başlatın
Terminali proje klasöründe açın ve şu komutu girin:

Bash

docker-compose up --build

İlk kurulumda gerekli kütüphanelerin indirilmesi internet hızınıza bağlı olarak birkaç dakika sürebilir.

4. Kullanım
Kurulum bittiğinde terminalde Running on local URL: http://0.0.0.0:7860 yazısını göreceksiniz. Tarayıcınızdan şu adrese gidin:

👉 http://localhost:7860
