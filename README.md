**Bu projeyi kullanmak için aşağıdaki adımları takip edebilirsiniz.**

**Gereksinimlerin Kurulumu:** Kullanılan araçlar Kali Linux işletim sisteminde hazır olarak gelen araçlardır. Bazı araçların çalışması için ek gereksinimler olabilir. Örneğin, pyfiglet modülünü kurmak için: pip3 install pyfiglet

**Root Yetkisi:** Bazı araçlar için root yetkisi gerektirebilir. Root yetkisi almak için terminalde bu komutu kullanabilirsiniz: sudo su

# kali-linux-kit
Bir grafik kullanıcı arayüzü (GUI) oluşturarak, Kali Linux tabanlı bir ağ güvenliği araç kiti için bir arayüz sunar. Kullanıcı arayüzü, farklı ağ güvenliği görevlerini gerçekleştirmek için seçenekler sunar ve kullanıcının seçimlerine göre ilgili araçları çağırır.

İşlevsellik olarak şu özelliklere sahiptir:

**MAC Adresi Değiştirme:**  Kullanıcıya, bir ağ arayüzünün (örneğin, eth0 veya wlan0) MAC adresini değiştirme seçeneği sunar.

**Bilgi Toplama:** Kullanıcıya çeşitli bilgi toplama araçlarına erişim sağlar. Bu araçlar, hedef alan adı veya IP adresi için bilgi toplama işlemlerini gerçekleştirir. Örneğin, Dmitry, TheHarvester, Netdiscover, WAF, Dirb ve DNS araçlarına erişim sağlar.

**Ağ Taramaları:** Kullanıcıya çeşitli ağ tarama seçenekleri sunar. Bu seçenekler arasında servis ve versiyon taraması, script taraması, ayrıntılı tarama, tüm TCP taraması, tüm UDP taraması ve işletim sistemi tespiti bulunur.

**SearchSploit:** Kullanıcıya, belirli bir anahtar kelime ile zafiyet veritabanında arama yapma yeteneği sağlar.

**Nikto Tarama:** Kullanıcıya, web sunucularını ve uygulamaları hedefleyen güvenlik açıklarını tespit etmek için Nikto aracını kullanma yeteneği sağlar.

**Exiftool:** Kullanıcıya, dijital resim dosyalarının içeriğini analiz etmek için Exiftool'u kullanma yeteneği sağlar.

**Wordpress Tarama:** Kullanıcıya, belirli bir Wordpress sitesinde güvenlik zafiyetlerini tespit etmek için wpscan aracını kullanma yeteneği sağlar.

**Wordlist Oluşturma:** Kullanıcıya, belirli kriterlere göre özelleştirilmiş bir wordlist oluşturma yeteneği sağlar. Bu genellikle parola saldırıları için kullanılır.

Kullanıcı, GUI üzerinden bu işlevleri seçerek istediği ağ güvenlik testlerini gerçekleştirebilir. Kullanıcı arayüzü için Tkinter kütüphanesi kullanılmıştır. Tkinter, Python ile kolayca entegre edilebilen bir GUI kütüphanesidir.



![Ekran görüntüsü 2024-05-11 031838](https://github.com/oznursm/kali-linux-kit/assets/106736591/31df917d-c353-4aa7-997b-b54610002ab6)




