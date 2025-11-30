# 🐍 Python Tabanlı Kali Linux Araç Kiti

Bu proje, Kali Linux üzerinde sık kullanılan birçok siber güvenlik aracını tek bir Tkinter arayüzü üzerinden çalıştırmayı sağlayan **Python tabanlı bir GUI uygulamasıdır**.  
Amaç, terminalde uzun komutlar yazmak yerine tek tıklamayla otomasyon sağlamaktır.

---

## 🚀 Özellikler

### 🔧 MAC Adresi Değiştirme
- Rastgele MAC adresi üretir.
- Kullanıcıdan interface bilgisi alır (eth0, wlan0 vb.).

### 🕵️ Bilgi Toplama
Aşağıdaki araçları tek ekrandan çalıştırabilirsiniz:
- **Dmitry**
- **theHarvester**
- **Netdiscover**
- **Wafw00f**
- **Dirb**
- **Dnsenum**

### 🌐 Ağ Taramaları (Nmap)
- Servis ve versiyon taraması  
- Script taraması  
- Ayrıntılı tarama (-A)  
- Tüm TCP port taraması  
- Tüm UDP port taraması  
- İşletim sistemi tespiti  

### 🛡️ Searchsploit
- Belirtilen servis/uygulama için Exploit Database üzerinde zafiyet araması yapar.

### 🌍 Web Zafiyeti Taraması – Nikto
- Standart web taraması  
- SQL Injection odaklı tarama  
- XSS taraması  

### 🖼️ Görsel Analiz – Exiftool
- Resim dosyalarının meta verilerini inceleme.

### 📰 WordPress Güvenlik Taraması – WPScan
- Genel site taraması  
- Eklenti bilgisi çıkarma  
- Eklenti açıkları taraması  
- Tema tespiti  
- Tema açıklıkları  

### 📝 Kişiye Özel Wordlist Oluşturma – Crunch
- Minimum/maximum karakter  
- İçerik karakterleri  
- Dosya adı seçme  

---

## 📸 Arayüz Görseli

![Ekran görüntüsü 2024-05-11 031838](https://github.com/oznursm/kali-linux-kit/assets/106736591/31df917d-c353-4aa7-997b-b54610002ab6)

---

## 📦 Gereksinimler

### 🔧 Python Modülleri
```bash
pip install pyfiglet
```

## 🔧 Kali Linux Araçları (Zorunlu)

Bu uygulamanın çalışması için aşağıdaki araçların sistemde kurulu olması gerekmektedir:

- **macchanger**
- **dmitry**
- **theHarvester**
- **netdiscover**
- **wafw00f**
- **dirb**
- **dnsenum**
- **nmap**
- **searchsploit**
- **nikto**
- **exiftool**
- **wpscan**
- **crunch**

---

## 🛠️ Kurulum ve Çalıştırma

### 🔹 Depoyu klonlayın:
```bash
git clone https://github.com/oznursm/kali-linux-kit.git
```
### 🔹 Dizine girin:
```bash
cd kali-linux-kit
```

### 🔹 Uygulamayı çalıştırın:
```bash
python3 functions.py
```

Program açıldığında grafik arayüz görüntülenecek ve tüm işlemleri buradan seçebileceksiniz.

### ⚠️ Yasal Uyarı

Bu uygulama sadece izin verilen sistemlerde kullanılmalıdır.

İzinsiz sızma testi yapmak yasa dışıdır ve suçtur.

Bu proje yalnızca eğitim, öğrenme ve etik siber güvenlik amaçları için geliştirilmiştir.


