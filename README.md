🧠 BioMentor – AI Destekli Kişisel Sağlık Asistanı
YZTA Bootcamp | 3. Sprint Final Teslimi

🎯 Proje Vizyonu
BioMentor, bireylerin kişisel sağlık hedeflerine uygun olarak yapay zekâ destekli öneriler sunan bir asistan uygulamasıdır.

Başlıca özellikler:
✅ Kullanıcı, hedefini seçip 7 günlük kişisel plan alabilir.
✅ Mentor’e Sor özelliğiyle doğal dilde soru sorabilir.
✅ Kendini Test Et ile 10 soruluk mini test doldurabilir.

🚀 Sprint 3'te Tamamlananlar
✔️ Tam çalışan frontend-backend entegrasyonu sağlandı.
✔️ FastAPI tabanlı backend kuruldu, Gemini Pro API entegre edildi.
✔️ Hedef seçme → 7 günlük plan oluşturma özelliği tamamlandı.
✔️ Mentor’e Sor ekranı geliştirildi.
✔️ Kendini Test Et özelliği eklendi.
✔️ Arayüz, TailwindCSS ile modern ve animasyonlu hâle getirildi.

📸 Uygulama Görselleri
Ana ekran

Hedef seçme ve plan ekranı

Mentor’e Sor ekranı

Kendini Test Et ekranı

(Ekran görüntülerini buraya ekleyeceksin.)

📂 Proje Yapısı
bash
Kopyala
Düzenle
BioMentor/
│── backend/
│   └── app.py           # FastAPI backend
│── index.html           # Frontend ana dosya
│── requirements.txt     # Gerekli kütüphaneler
🔄 Sprint 2'den Sprint 3'e Gelişim
📌 Sprint 2: Planlama, mimari ve teknoloji seçimleri yapılmıştı.
📌 Sprint 3: Çalışan bir prototip tamamlandı.

📉 Çıkarılan Özellikler:

Tahlil dosyası (PDF) yükleme ve otomatik analiz

Veritabanına kullanıcı kayıt ve geri bildirim kaydı

Oturum yönetimi

Bu özellikler gelecek aşamada eklenmek üzere ertelendi.

📌 Kullanıcı Akışı
1️⃣ Ana ekran → "Hedefini Seç", "Mentor’e Sor", "Kendini Test Et"
2️⃣ Hedefini Seç → 7 günlük plan oluşturulur.
3️⃣ Mentor’e Sor → Kullanıcı doğal dilde soru sorar, AI yanıt verir.
4️⃣ Kendini Test Et → 10 soruluk test doldurulur, ardından basit bir özet sonucu gösterilir.

🤖 Kullanılan Teknolojiler
Katman	Teknoloji
Frontend	HTML, CSS (Tailwind), JS
Backend	Python (FastAPI, Uvicorn)
AI	Google Gemini Pro API

🔜 Sonraki Adımlar
✅ Render veya benzeri platformda deploy edilecek.
✅ Küçük hatalar (örn. test sonucu özeti, API yanıt formatı) düzeltilecek.
