---
id: tool-05509
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/betulerkocc/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5509
category: 一、去 AI 味 / Humanizer 库
repo: betulerkocc/ai-text-detector
stars: 0
url: https://github.com/betulerkocc/ai-text-detector
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
content_hash: 8c201c00228be1f3
  - methods/改稿润色指令库.md
---

# betulerkocc/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/betulerkocc/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：betulerkocc/ai-text-detector
- **拉取时间**：2026-07-25 18:21:20

---

# 🤖 AI vs. Human - Yapay Zeka Metin Tespit Sistemi

Bu proje, girilen makale, ödev veya deneme yazısı (essay) metinlerini gelişmiş Doğal Dil İşleme (NLP) ve Makine Öğrenmesi teknikleriyle analiz ederek bir **insan** tarafından mı yoksa **Yapay Zeka (ChatGPT, Claude vb.)** tarafından mı üretildiğini tahmin eden uçtan uca bir yazılım sistemidir.

---

## 🎬 Proje Canlı Demo Videosu
Uygulamanın çalıştığını, dosya yükleme fonksiyonunu ve gerçek zamanlı tahmin performansını gösteren kısa demo videosuna aşağıdaki bağlantıdan ulaşabilirsiniz:
👉 https://youtu.be/PW07eBft9zE

## 🛠️ Proje Mimarisi ve Klasör Yapısı
Proje, temiz kod (clean code) prensiplerine uygun, nesne yönelimli, modüler ve genişletilebilir bir mimariyle tasarlanmıştır:

```text
ai-text-detector/
│
├── data/                   # Eğitimde kullanılan Kaggle veri seti (.csv)
├── models/                 # Eğitilmiş yapay zeka modeli ve vektörizer (.pkl)
│
├── src/                    # Projenin motor odası (Modüler Python Kodları)
│   ├── __init__.py         # src klasörünü paket (package) olarak tanımlar
│   ├── preprocessing.py    # Metin temizleme sınıfı (TextPreprocessor)
│   └── train.py            # Model eğitimi ve metrik değerlendirme scripti
│
├── app.py                  # Streamlit interaktif kullanıcı arayüzü (Web App)
├── requirements.txt        # Gerekli kütüphaneler listesi
└── README.md               # Proje dokümantasyonu

## 🧼 Metin Ön İşleme ve Zaman Karmaşıklığı (Time Complexity)

Projenin `src/preprocessing.py` modülü altında geliştirilen `TextPreprocessor` sınıfı, ham metinleri yapay zekanın anlayabileceği standart forma dönüştürür.

* **Optimizasyon:** Kelime temizleme süreçlerinde arama hızını maksimuma çıkarmak için NLTK stopword listesi `set` (küme) veri tipine dönüştürülmüştür. Böylece eleman arama maliyeti $O(N)$'den **$O(1)$** seviyesine düşürülmüştür.
* **Toplam Zaman Karmaşıklığı:** $O(W)$ -> ($W$: Metindeki toplam kelime sayısıdır). Metin boyutuna göre optimum sürede çalışır.

---

## 📊 Model Eğitimi ve Başarı Metrikleri

Model, Kaggle üzerindeki gerçek insan yazıları ve LLM (Yapay Zeka) tarafından türetilmiş binlerce akademik deneme yazısından oluşan dengeli bir veri setiyle eğitilmiştir. Metinleri sayısallaştırmak için kelime ikililerini de yakalayabilen **TF-IDF (Unigram & Bigram)** tekniği kullanılmış, sınıflandırma mimarisinde ise **Logistic Regression** tercih edilmiştir.

Modelin test seti üzerinde yakaladığı üstün başarı metrikleri şu şekildedir:

* **Genel Doğruluk (Accuracy):** %94.88
* **İnsan Metinleri F1-Score:** %0.95
* **Yapay Zeka Metinleri F1-Score:** %0.95

> **💡 Mühendislik Notu (Threshold Ayarı):** Gerçek hayattaki kurallı ve temiz insan metinlerinin yapay zeka kelime havuzuna benzerliğinden kaynaklanan hatalı sınıflandırmaları önlemek amacıyla, sistemin karar sınırına **%70 Eşik Değer (Threshold)** filtresi entegre edilmiştir. Model yapay zeka olduğundan %70'ten fazla emin değilse, metni insan yazımı olarak kabul ederek sahte pozitif (false positive) oranını minimize eder.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 🚀 Kurulum ve Çalıştırma Talimatı

### 1. Bağımlılıklerin Kurulması
Terminali açarak proje dizininde aşağıdaki komutu çalıştırıp gerekli tüm kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt

### 2. Modelin Eğitilmesi
Veri setini işleyip modeli eğitmek ve models/ klasörüne kaydetmek için şu komutu çalıştırın:
python src/train.py

### 3. Web Arayüzünün Başlatılması
Streamlit tabanlı interaktif web arayüzünü canlıya almak için şu komutu çalıştırın:
streamlit run app.py

Uygulama başarıyla ayağa kalktığında tarayıcınız üzerinden otomatik olarak veya http://127.0.0.1:8501 adresinden sisteme erişebilirsiniz.

## 🖥️ Fonksiyonel Özellikler

* Metin Alanı Girişi: Kullanıcılar analiz etmek istedikleri metinleri doğrudan kopyalayıp yapıştırabilir.

* Dosya Yükleme Desteği: Kullanıcılar .txt uzantılı ödev veya makale dosyalarını sisteme yükleyerek gerçek zamanlı analiz gerçekleştirebilir.

* Güven Oranı Metriği: Sistem sadece 0-1 tahmini yapmakla kalmaz, tahminin arkasındaki yapay zeka veya insan olma olasılığını yüzde cinsinden canlı gösterir.
