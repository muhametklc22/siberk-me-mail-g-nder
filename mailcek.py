import requests
from bs4 import BeautifulSoup
import re
import time

# Tüm sayfalardaki e-posta adreslerini saklamak için liste
all_emails = set()  
url_template = "https://www.siberkume.org.tr/uyeler?page={}"

# Sayfaları dolaşmak için döngü
for page_num in range(1, 14):  # 1'den 13'e kadar sayfa numaraları
    url = url_template.format(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Sayfadaki e-posta adreslerini bul
    for link in soup.find_all('a', href=True):
        if "mailto:" in link['href']:
            email = link['href'].replace("mailto:", "")
            all_emails.add(email)
    
    # Çok hızlı istek göndermemek için kısa bir bekleme süresi
    time.sleep(1)  

# E-posta adreslerini mailler.txt dosyasına kaydetme
with open("mailler.txt", "w") as file:
    for email in all_emails:
        file.write(email + "\n")

print("E-posta adresleri mailler.txt dosyasına kaydedildi.")
