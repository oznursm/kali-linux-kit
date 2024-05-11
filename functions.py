import tkinter as tk  # Tkinter kütüphanesi
import os  # Komutları çalıştırmak için
import pyfiglet # type: ignore
from tkinter import simpledialog, messagebox  # Kullanıcı girişi ve hata/uyarı mesajları için

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Python Tabanlı Kali Linux Arac Kiti")
root.geometry("400x400")  # Ana pencere boyutu

# Pyfiglet ile başlık
figlet_kit = pyfiglet.figlet_format("Python Tabanlı Kali Linux Arac Kiti", font="standard")
label = tk.Label(root, text=figlet_kit, font=("Courier", 10), justify="center")
label.pack()

# Her seçim için yeni pencere açan fonksiyonlar
def open_mac_window():
    new_window = tk.Toplevel(root)
    new_window.title("MAC Adresi Değiştirme")
    new_window.geometry("300x200")
    interface = simpledialog.askstring("Interface Seç", "MAC adresini değiştirmek istediğiniz interface girin (eth0, wlan0):", parent=new_window)
    os.system(f"macchanger -r {interface}")

def open_info_window():
    new_window = tk.Toplevel(root)
    new_window.title("Bilgi Toplama")
    new_window.geometry("300x200")
    info_option = simpledialog.askinteger("Bilgi Toplama Seçeneği", "1: Dmitry Aracı, 2: TheHarvester Aracı, 3: Local Ağdaki Cihazları Göster(Netdiscover), 4: Hedef Adreste Güvenlik Duvarı Kontrol, 5: Dizin Taraması(Dirb), 6: DNS Taraması", parent=new_window)

    if info_option == 1:
        domain = simpledialog.askstring("Dmitry Aracı", "Sorgulanacak Alan adı:", parent=new_window)
        os.system(f"dmitry -winsep {domain}")
    elif info_option == 2:
        domain = simpledialog.askstring("TheHarvester Aracı", "Sorgulanacak Alan adı:", parent=new_window)
        os.system(f"theHarvester -d {domain} -l 500 -b all")
    elif info_option == 3:
        os.system("netdiscover")
    elif info_option == 4:
        domain = simpledialog.askstring("Güvenlik Duvarı Kontrol", "Sorgulanacak alan adı:", parent=new_window)
        os.system(f"wafw00f -a {domain}")
    elif info_option == 5:
        domain = simpledialog.askstring("Dizin Taraması", "Dizin Sorgusu Yapılacak alan adı:", parent=new_window)
        os.system(f"dirb {domain}")
    elif info_option == 6:
        domain = simpledialog.askstring("DNS Taraması", "DNS Sorgusu için alan adı:", parent=new_window)
        os.system(f"dnsenum {domain}")
    else:
        messagebox.showerror("Hata", "Geçersiz seçim")

def open_nmap_window():
    new_window = tk.Toplevel(root)
    new_window.title("Ağ Taramaları(Nmap)")
    new_window.geometry("300x200")
    nmap_option = simpledialog.askinteger("Ağ Taramaları(Nmap)", "1: Servis ve Versiyon Taraması, 2: Script Taraması, 3: Ayrıntılı Tarama, 4: Tüm TCP Portları Tara, 5: Tüm UDP Portları Tara, 6: OS Tespiti", parent=new_window)

    if nmap_option == 1:
        ip = simpledialog.askstring("Servis ve Versiyon Taraması", "Tarama yapılacak IP adresi:", parent=new_window)
        os.system(f"nmap -sS -sV {ip}")
    elif nmap_option == 2:
        ip = simpledialog.askstring("Script Taraması", "Tarama yapılacak IP adresi:", parent=new_window)
        os.system(f"nmap -sC {ip}")
    elif nmap_option == 3:
        ip = simpledialog.askstring("Ayrıntılı Tarama", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -A {ip}")
    elif nmap_option == 4:
        ip = simpledialog.askstring("Tüm TCP Portları Tara", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -sT {ip}")
    elif nmap_option == 5:
        ip = simpledialog.askstring("Tüm UDP Portları Tara", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -sU {ip}")
    elif nmap_option == 6:
        ip = simpledialog.askstring("OS Tespiti", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -O {ip}")

def open_searchsploit_window():
    new_window = tk.Toplevel(root)
    new_window.title("Hedefte Çıkmış Zafiyet Taraması(Searchsploit)")
    new_window.geometry("300x200")
    keyword = simpledialog.askstring("Hedefte Çıkmış Zafiyet Taraması(Searchsploit)", "Zafiyet Aranacak Anahtar Kelime (ör: Vsftpd):", parent=new_window)
    os.system(f"searchsploit {keyword}")

def open_nikto_window():
    new_window = tk.Toplevel(root)
    new_window.title("Hedefte Web Zafiyeti Taraması(Nikto)")
    new_window.geometry("300x200")
    nikto_option = simpledialog.askinteger("Hedefte Web Zafiyeti Taraması(Nikto)", "1: Web Sitesine Yönelik Standart Tarama, 2: SQL Injection Taraması, 3: XSS Taraması", parent=new_window)

    if nikto_option == 1:
        url = simpledialog.askstring("Web Sitesine Yönelik Standart Tarama", "Tarama yapılacak URL:", parent=new_window)
        os.system(f"nikto -h {url}")
    elif nikto_option == 2:
        url = simpledialog.askstring("SQL Injection Taraması", "Tarama yapılacak URL:", parent=new_window)
        os.system(f"nikto -h {url} -Cgidirs none -Tuning 9")
    elif nikto_option == 3:
        url = simpledialog.askstring("XSS Taraması", "Tarama yapılacak URL:", parent=new_window)
        os.system(f"nikto -h {url} -Cgidirs none -Tuning 4")

def open_exiftool_window():
    new_window = tk.Toplevel(root)
    new_window.title("Görsel Analiz(Exiftool)")
    new_window.geometry("300x200")
    image_path = simpledialog.askstring("Görsel Analiz(Exiftool)", "Analiz Yapılacak Resim Yolu:", parent=new_window)
    os.system(f"exiftool {image_path}")

def open_wordpress_window():
    new_window = tk.Toplevel(root)
    new_window.title("Wordpress Siteleri Tarama")
    new_window.geometry("300x200")
    wp_option = simpledialog.askinteger("Wordpress Siteleri Tarama", "1: Hedef Siteye Yönelik Genel Tarama, 2: Hedef Sitenin Eklentilerini Tespit Etme, 3: Kullanılan Tema Açıkları, 4: Sitede Kullanılan Tema", parent=new_window)

    if wp_option == 1:
        site = simpledialog.askstring("Hedef Siteye Yönelik Genel Tarama", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site}")
    elif wp_option == 2:
        site = simpledialog.askstring("Hedef Sitenin Eklentilerini Tespit Etme", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site} --enumerate p")
        response = simpledialog.askstring("Zafiyet Tarama", "Eklenti zafiyetleri taransın mı? (e/h):", parent=new_window)
        if response == 'e':
            os.system(f"wpscan --url {site} --enumerate ap")
    elif wp_option == 3:
        site = simpledialog.askstring("Kullanılan Tema Açıkları", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site} --enumerate at")
    elif wp_option == 4:
        site = simpledialog.askstring("Sitede Kullanılan Tema Bilgisi", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site} --enumerate t")

def open_wordlist_window():
    new_window = tk.Toplevel(root)
    new_window.title("Wordlist Oluşturma")
    new_window.geometry("300x200")
    min_char = simpledialog.askinteger("Minimum Karakter", "Wordlist minimum kaç karakter içermeli?", parent=new_window)
    max_char = simpledialog.askinteger("Maximum Karakter", "Wordlist maximum kaç karakter içermeli?", parent=new_window)
    content = simpledialog.askstring("İçerik", "Wordlist hangi karakterleri içermeli?", parent=new_window)
    filename = simpledialog.askstring("Dosya Adı", "Wordlist dosyanızın ismi:", parent=new_window)
    os.system(f"crunch {min_char} {max_char} {content} -o {filename}")

# Ana menü düğmeleri
tk.Button(root, text="MAC Adresi Değiştirme", command=open_mac_window).pack(pady=10)
tk.Button(root, text="Bilgi Toplama(Dmitry/theHarvester/Netdiscover/Wafw00f/Dirdb/Dnsenum)", command=open_info_window).pack(pady=10)
tk.Button(root, text="Ağ Taramaları(Nmap)", command=open_nmap_window).pack(pady=10)
tk.Button(root, text="Hedefte Çıkmış Zafiyet Taraması(Searchsploit)", command=open_searchsploit_window).pack(pady=10)
tk.Button(root, text="Hedefte Web Zafiyeti Taraması(Nikto)", command=open_nikto_window).pack(pady=10)
tk.Button(root, text="Görsel Analiz(Exiftool)", command=open_exiftool_window).pack(pady=10)
tk.Button(root, text="Wordpress Siteleri Tarama", command=open_wordpress_window).pack(pady=10)
tk.Button(root, text="Kişiye Özel Wordlist Oluşturma", command=open_wordlist_window).pack(pady=10)

# Ana pencereyi çalıştırmak için
root.mainloop()

