# 🧠 BioMentor – AI Destekli Kişisel Sağlık Asistanı

YZTA Bootcamp | 3. Sprint Final Teslimi

## 🎯 Proje Vizyonu

BioMentor, bireylerin kişisel sağlık hedeflerine yönelik, bilimsel temelli ve ilaçsız öneriler sunan bir yapay zekâ destekli asistan uygulamasıdır.

### Başlıca Özellikler

✅ Kullanıcı hedefini seçip 7 günlük kişisel plan alabilir.
✅ Mentor’e Sor özelliğiyle doğal dilde soru sorabilir.
✅ Kendini Test Et bölümünde 10 soruluk mini bir test doldurabilir.

---

## 🚀 Sprint 3'te Tamamlananlar

✔️ FastAPI tabanlı backend ve TailwindCSS tabanlı frontend tamamlandı.
✔️ Gemini Pro API entegre edilerek AI tabanlı öneriler sağlandı.
✔️ Hedef seçme → 7 günlük plan oluşturma özelliği geliştirildi.
✔️ Mentor’e Sor ve Kendini Test Et ekranları eklendi.
✔️ Modern ve animasyonlu bir arayüz tasarlandı.

---

## 📂 Proje Yapısı

```
BioMentor/
│── backend/
│   └── app.py          # FastAPI backend
│── index.html          # Frontend ana dosya
│── requirements.txt    # Kullanılan kütüphaneler
```

---

## 🔄 Sprint 2'den Sprint 3'e Gelişim

📌 Sprint 2’de mimari planlama, teknoloji seçimi ve akış tasarımı yapılmıştı.
📌 Sprint 3’te çalışan bir prototip tamamlandı.

---

## 📉 Çıkarılan Özellikler ve Nedenleri

1️⃣ **Tahlil dosyası yükleme ve otomatik analiz**
➡️ KVKK ve veri güvenliği nedeniyle bu özellik bu sprintte devre dışı bırakıldı.

2️⃣ **Veritabanı ve kullanıcı kayıt sistemi**
➡️ Tek kişilik yürütülen proje için bu sprintte öncelik temel özelliklere verildi.

3️⃣ **Oturum yönetimi (login/logout)**
➡️ Kullanıcı kaydı olmadığı için bu özellik de ertelendi.

---

## 📌 Kullanıcı Akışı

1️⃣ Ana ekran → "Hedefini Seç", "Mentor’e Sor", "Kendini Test Et"
2️⃣ Hedefini Seç → 7 günlük plan oluşturulur.
3️⃣ Mentor’e Sor → Kullanıcı doğal dilde soru sorar, AI yanıt verir.
4️⃣ Kendini Test Et → 10 soruluk test doldurulur, ardından özet sonuç gösterilir.

---

## 🤖 Kullanılan Teknolojiler

| Katman   | Teknoloji                 |
| -------- | ------------------------- |
| Frontend | HTML, CSS (Tailwind), JS  |
| Backend  | Python (FastAPI, Uvicorn) |
| AI       | Google Gemini Pro API     |

---

## 🔜 Sonraki Adımlar

✅ Render veya benzeri platformda canlıya alınacak.
✅ Test sonucu özeti ve AI yanıt formatı geliştirilecek.
✅ KVKK uyumlu şekilde tahlil yükleme ve kullanıcı kayıt özellikleri eklenecek.
