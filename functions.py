import tkinter as tk  # Tkinter kütüphanesi
import os  # Komutları çalıştırmak için
import pyfiglet
from tkinter import simpledialog, messagebox  # Kullanıcı girişi ve hata/uyarı mesajları için

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Network - Security - Kit")
root.geometry("400x400")  # Ana pencere boyutu

# Pyfiglet ile başlık
figlet_kit = pyfiglet.figlet_format("Python Tabanlı Kali Linux Araç Kiti", font="standard")
label = tk.Label(root, text=figlet_kit, font=("Courier", 10), justify="center")
label.pack()

# Her seçim için yeni pencere açan fonksiyonlar
def open_mac_window():
    new_window = tk.Toplevel(root)
    new_window.title("MAC Adresi Değiştir")
    new_window.geometry("300x200")
    interface = simpledialog.askstring("Interface Seç", "MAC adresini değiştirmek istediğiniz arayüzü girin (eth0, wlan0):", parent=new_window)
    os.system(f"macchanger -r {interface}")

def open_info_window():
    new_window = tk.Toplevel(root)
    new_window.title("Bilgi Toplama")
    new_window.geometry("300x200")
    info_option = simpledialog.askinteger("Bilgi Toplama Seçeneği", "1: Dmitry, 2: TheHarvester, 3: Netdiscover, 4: WAF, 5: Dirb, 6: DNS", parent=new_window)

    if info_option == 1:
        domain = simpledialog.askstring("Dmitry", "Sorgulanacak alan adı:", parent=new_window)
        os.system(f"dmitry -winsep {domain}")
    elif info_option == 2:
        domain = simpledialog.askstring("TheHarvester", "Sorgulanacak alan adı:", parent=new_window)
        os.system(f"theHarvester -d {domain} -l 500 -b all")
    elif info_option == 3:
        os.system("netdiscover")
    elif info_option == 4:
        domain = simpledialog.askstring("WAF Kontrol", "Sorgulanacak alan adı:", parent=new_window)
        os.system(f"wafw00f -a {domain}")
    elif info_option == 5:
        domain = simpledialog.askstring("Dirb", "Sorgulanacak dizin:", parent=new_window)
        os.system(f"dirb {domain}")
    elif info_option == 6:
        domain = simpledialog.askstring("DNS Enum", "DNS Sorgusu için alan adı:", parent=new_window)
        os.system(f"dnsenum {domain}")
    else:
        messagebox.showerror("Hata", "Geçersiz seçim")

def open_nmap_window():
    new_window = tk.Toplevel(root)
    new_window.title("Ağ Taramaları")
    new_window.geometry("300x200")
    nmap_option = simpledialog.askinteger("Nmap Seçeneği", "1: Servis ve Versiyon, 2: Script, 3: Ayrıntılı, 4: Tüm TCP, 5: Tüm UDP, 6: OS Tespiti", parent=new_window)

    if nmap_option == 1:
        ip = simpledialog.askstring("Tarama", "Tarama yapılacak IP adresi:", parent=new_window)
        os.system(f"nmap -sS -sV {ip}")
    elif nmap_option == 2:
        ip = simpledialog.askstring("Script Tarama", "Tarama yapılacak IP adresi:", parent=new_window)
        os.system(f"nmap -sC {ip}")
    elif nmap_option == 3:
        ip = simpledialog.askstring("Ayrıntılı Tarama", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -A {ip}")
    elif nmap_option == 4:
        ip = simpledialog.askstring("Tüm TCP", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -sT {ip}")
    elif nmap_option == 5:
        ip = simpledialog.askstring("Tüm UDP", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -sU {ip}")
    elif nmap_option == 6:
        ip = simpledialog.askstring("OS Tespiti", "Tarama yapılacak IP:", parent=new_window)
        os.system(f"nmap -O {ip}")

def open_searchsploit_window():
    new_window = tk.Toplevel(root)
    new_window.title("SearchSploit")
    new_window.geometry("300x200")
    keyword = simpledialog.askstring("SearchSploit", "Zafiyet aranacak anahtar kelime (ör: Vsftpd):", parent=new_window)
    os.system(f"searchsploit {keyword}")

def open_nikto_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nikto Tarama")
    new_window.geometry("300x200")
    nikto_option = simpledialog.askinteger("Nikto Tarama Seçeneği", "1: Standart Tarama, 2: SQL Injection Taraması, 3: XSS Taraması", parent=new_window)

    if nikto_option == 1:
        url = simpledialog.askstring("Standart Tarama", "Tarama yapılacak URL:", parent=new_window)
        os.system(f"nikto -h {url}")
    elif nikto_option == 2:
        url = simpledialog.askstring("SQL Injection", "Tarama yapılacak URL:", parent=new_window)
        os.system(f"nikto -h {url} -Cgidirs none -Tuning 9")
    elif nikto_option == 3:
        url = simpledialog.askstring("XSS Taraması", "Tarama yapılacak URL:", parent=new_window)
        os.system(f"nikto -h {url} -Cgidirs none -Tuning 4")

def open_exiftool_window():
    new_window = tk.Toplevel(root)
    new_window.title("Exiftool")
    new_window.geometry("300x200")
    image_path = simpledialog.askstring("Exiftool", "Analiz yapılacak resim yolu:", parent=new_window)
    os.system(f"exiftool {image_path}")

def open_wordpress_window():
    new_window = tk.Toplevel(root)
    new_window.title("Wordpress Tarama")
    new_window.geometry("300x200")
    wp_option = simpledialog.askinteger("Wordpress Seçeneği", "1: Genel Tarama, 2: Eklentiler, 3: Tema Açıkları, 4: Kullanılan Tema Bilgisi", parent=new_window)

    if wp_option == 1:
        site = simpledialog.askstring("Genel Tarama", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site}")
    elif wp_option == 2:
        site = simpledialog.askstring("Eklentiler", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site} --enumerate p")
        response = simpledialog.askstring("Zafiyet Tarama", "Eklenti zafiyetleri taransın mı? (e/h):", parent=new_window)
        if response == 'e':
            os.system(f"wpscan --url {site} --enumerate ap")
    elif wp_option == 3:
        site = simpledialog.askstring("Tema Açıkları", "Taranacak site:", parent=new_window)
        os.system(f"wpscan --url {site} --enumerate at")
    elif wp_option == 4:
        site = simpledialog.askstring("Kullanılan Tema", "Taranacak site:", parent=new_window)
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
tk.Button(root, text="MAC Adresi Değiştir", command=open_mac_window).pack(pady=10)
tk.Button(root, text="Bilgi Toplama", command=open_info_window).pack(pady=10)
tk.Button(root, text="Ağ Taramaları", command=open_nmap_window).pack(pady=10)
tk.Button(root, text="SearchSploit", command=open_searchsploit_window).pack(pady=10)
tk.Button(root, text="Nikto Tarama", command=open_nikto_window).pack(pady=10)
tk.Button(root, text="Exiftool", command=open_exiftool_window).pack(pady=10)
tk.Button(root, text="Wordpress Tarama", command=open_wordpress_window).pack(pady=10)
tk.Button(root, text="Wordlist Oluşturma", command=open_wordlist_window).pack(pady=10)

# Ana pencereyi çalıştırmak için
root.mainloop()
