# 🧠 BioMentor – AI Destekli Kişisel Sağlık Asistanı  
**YZTA Bootcamp | 2. Sprint Teslimi**

---

## 🎯 Proje Vizyonu

**BioMentor**, bireylerin kan tahlili sonuçlarını analiz ederek eksik çıkan değerler (örneğin B12, D vitamini, demir vb.) için **ilaçsız**, **doğal**, **yaşam tarzına uygun** ve **bilimsel kaynaklı** öneriler sunan bir yapay zekâ destekli sağlık destek sistemidir.

Uygulama, hem otomatik analiz motoru hem de kullanıcı ile doğal dilde konuşabilen bir AI modülünü bünyesinde barındırır. Bu sayede kullanıcılar sadece verilerini girerek öneri almaz, aynı zamanda "kefir içemiyorum, bana alternatif probiyotik önerir misin?" gibi kişisel sorular da yöneltebilir.

---

## 🛠️ 2. Sprint Özeti

Sprint 2 sürecinde proje teknik olarak ilerletilememiş olabilir; **ancak fikrin temelleri sağlamlaştırılmış, teknoloji planlaması yapılmış ve proje yönü netleştirilmiştir.**  
Üstelik proje, bu sprint sırasında **tek kişilik hale gelmiştir.**

Buna rağmen:

✅ Proje fikri güncellendi ve netleştirildi  
✅ Kullanıcı akışı, senaryolar ve teknik yapılar belirlendi  
✅ Kullanılacak yapay zekâ modeli (Gemini Pro API) kararlaştırıldı  
✅ AI fonksiyonları için `features/qa_chat.py` dosyası oluşturuldu  
✅ README ve dökümantasyon içerikleri hazırlandı

🟡 Kodlama süreci Sprint 3’e ertelendi.

---

## 🧩 Jüriye Kısa Mesajım:

> “Evet, tek başıma kaldım ama fikrim net, AI planım hazır, Sprint 3’te kodlayacağım.”

Bu teslimle sıfırdan bir yapı kurulmuş, teknik yol haritası hazırlanmış ve AI entegrasyonu için gerçekçi bir temel atılmıştır.

---

## 💡 Kullanıcı Deneyimi Özeti

- Kullanıcı tahlil verisini (PDF ya da manuel) sisteme girer  
- Sistem, eksik değerleri referans aralıklarıyla kıyaslayarak tespit eder  
- Her eksik değer için AI modeli (Gemini) tarafından öneriler üretilir  
- Kullanıcı ayrıca doğal dilde sorular sorabilir ve kişiselleştirilmiş öneriler alabilir  
- Önerilerin altında mutlaka bilimsel kaynak ve “tıbbi tavsiye değildir” uyarısı bulunur  
- Kullanıcı, önerilere geri bildirim vererek sistemin öğrenmesini destekler  

---

## 🤖 Kullanılan / Kullanılacak Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Frontend | React.js, TailwindCSS |
| Backend | Python, FastAPI |
| Veritabanı | PostgreSQL |
| AI | Google Gemini Pro API |
| Veri Analizi | Pandas, NumPy |
| OCR | pdfplumber, Tesseract |
| Prototip | Streamlit / Gradio (isteğe bağlı) |

---

## 📂 Mevcut Dosya ve Yapı

- `README.md` → Proje açıklaması ve dökümantasyon  
- `features/qa_chat.py` → AI öneri fonksiyonu başlangıç dosyası  
- `requirements.txt` → Kullanılacak temel kütüphaneler (örnek: `requests`)  

---

## 🧭 Bir Sonraki Sprint’te (Sprint 3)

- Kullanıcıdan gelen tahlil değerlerini referanslarla analiz edecek altyapı kurulacak  
- Gemini API ile öneriler dinamik olarak üretilecek  
- Manuel değer girişi formu ve öneri ekranı prototip olarak tasarlanacak  
- Doğal dilde soru-cevap sistemi aktif hâle getirilecek  
- AI cevaplarının doğruluğu ve kaynakları test edilecek  

---

Bu sprint bir geçiş dönemiydi — koddan çok planlama sprintiydi.  
Ama Sprint 3’te projenin ilk çalışan modüllerini teslim edeceğim.
