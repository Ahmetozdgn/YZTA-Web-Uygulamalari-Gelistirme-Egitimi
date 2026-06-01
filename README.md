# 📚 Web Uygulamaları Geliştirme — Atıl Samancıoğlu Takip Notları

Yapay Zeka ve Teknoloji Akademisi (YZTA) bünyesinde Atıl Samancıoğlu tarafından verilen Web Uygulamaları Geliştirme başlıklı eğitimin uygulamalı kod çalışmalarıdır.

🎯 **Proje Hakkında**
Bu repo, eğitim sürecinde anlatılan konuların ve mimari yapıların canlı olarak yazılan kodlar üzerinden bire bir takip edilerek yeniden uygulanmasından oluşmaktadır. Amaç; asenkron backend mimarisini, veritabanı ilişkilerini ve modern API standartlarını pratik yaparak pekiştirmektir.

⚠️ **Not:** Bu repoda yalnızca uygulama kodları, şemalar ve konfigürasyon dosyaları bulunmaktadır. Eğitimin sözel/teorik kısmı dahil edilmemiştir.

🗂️ **Klasör Yapısı**

```text
WEB_UYGULAMALARI/
│
├── 1Pydantic/                          # Pydantic ile Veri Modelleme ve Validasyon
│   ├── main1.py
│   ├── main1-2(konuaçıklama).py
│   ├── main2pydantic.py
│   └── main2pydantic(konuanlatım).py
│
├── 2AsyncExplained/                    # Python'da Asenkron Programlama Temelleri
│   ├── main.py
│   ├── main2.py
│   ├── mainasync(konuanlatım).py
│   └── mainasync.py
│
├── 3FastAPItemelleri/                  # HTTP Protokolleri ve API Temelleri
│   ├── 1FastCrud/
│   ├── 2HTTP Protokolleri/
│   ├── 3JSONnedir/
│   ├── 4IlkGET islemi/
│   ├── 5PathParametreleri/
│   ├── 6pathcakismalari/
│   ├── 7QueryileFiltreleme/
│   ├── 8PathveQueryAyniAnda/
│   ├── 9PostIslemi/
│   └── 10UpdateveDelete/
│
├── 4FastAPIOrtaSeviye/                 # Status Kodları ve Model Yönetimi
│   ├── 1StatusKodlan/
│   ├── 2ModelveMockDB/
│   ├── 3StatusCodeSecimleri/
│   ├── 4Path Islemleri/
│   ├── 5QueryIslemleri/
│   ├── 6PydanticIstekler/
│   ├── 7GuncellemeFonksiyonu/
│   └── 8SilmeIslemiveSonrakiAdimlar/
│
├── 5Veritabanɪİşlemleri/               # SQLAlchemy ORM Entegrasyonu
│   ├── 1Select İşlemleri/
│   ├── 2Girdiler/
│   ├── 3Guncelleme ve Silme/
│   └── 4TodoGemini/
│
├── 6Dependency Injection/              # FastAPI Depends Mekanizması
│   ├── 1DependencyInjectionpython/
│   ├── 2DependencyInjection/
│   ├── 3TodoGemini/
│   ├── 4TodoGeminiIDyeGoreFiltrelemeYapmak/
│   ├── 5TodoGeminiVeriekleme/
│   └── 6TodoGeminiUpdateveDeleteİşlemleri/
│
├── 7Yetkinlendirme İşlemleri/           # OAuth2, JWT ve Güvenlik
│   ├── 1TodoGeminiRouterMantıği/
│   ├── 2TodoGeminiRouterYapisi/
│   ├── 3UserTablosu/
│   ├── 4IlkIselTabloIncelemesi/
│   ├── 5ParolaveŞifreİlişkisi/
│   ├── 6GirisYapmaMantigi/
│   ├── 7JWT_Encoding_Decoding/
│   ├── 8IstekLimitlemeleri/
│   └── 9SilmeGuncellemeOkumaLimitleri/
│
├── 8Migrationİşlemleri/                # Alembic ile Veritabanı Versiyonlama
│   ├── 1AlembicNedir_Migration İşlemi/
│   └── Alembic notları/
│
├── 9FrontEnd/                          # Jinja2 Templates ve Statik Dosyalar
│   ├── static/
│   ├── templates/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── todoai_app.db
│
├── 10Gemini/                           # Yapay Zeka (LLM) Entegrasyonu
│   └── ToDoWithGemini/
│
└── 11Docker/                           # Konteynerizasyon İşlemleri
    └── ToDoGeminiApp-main/

🔬 Modül Detayları

FastAPI & Pydantic: Veri doğrulama, tip güvenliği ve otomatik validasyon süreçleri.

Asenkron Mimari: async/await ile bloklanmayan I/O operasyonları ve yüksek performanslı API tasarımı.

Veritabanı & ORM: SQLAlchemy ile ilişkisel veritabanı yönetimi ve Alembic ile şema versiyonlama.

Güvenlik (Security): JWT tabanlı yetkilendirme, şifreleme algoritmaları ve güvenli router yapıları.

Frontend & AI: Jinja2 template motoru ile arayüz geliştirme ve Google Gemini API entegrasyonu.

DevOps: Uygulamanın Docker mimarisine taşınması ve ortam bağımsız çalıştırılması.

🛠️ Kullanılan Teknolojiler

Backend: FastAPI, Pydantic, Python (Async)

Veritabanı: SQLite, SQLAlchemy, Alembic

Güvenlik: JWT, Bcrypt, Passlib

Frontend: Jinja2, HTML5, Bootstrap

DevOps & AI: Docker, Docker Compose, Google Gemini API

🚀 Kurulum

# Sanal ortam oluşturun ve aktif edin
python -m venv venv
source venv/Scripts/activate  # Windows için

# Bağımlılıkları yükleyin
pip install -r requirements.txt
