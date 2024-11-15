import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

# SMTP Sunucusu Bilgileri
smtp_server = "smtp.gmail.com"  # Örneğin Gmail için
smtp_port = 587
username = "muhamrt546@gmail.com"  # Gönderen e-posta adresi
password = "wasxpcuvnpjeqeqi"    # E-posta şifreniz veya uygulama şifresi

# E-posta İçeriği
subject = "Staj Başvurusu"
body = """Merhaba,

Gelecek dönem için üniversitemin zorunlu staj programı kapsamında uzun dönem bir iş yeri eğitimi arayışındayım. Siber güvenlik, ağ yönetimi ve bilgi güvenliği alanlarında teorik bilgiye sahibim ve bu bilgileri uygulamalı olarak pekiştirmek için şirketinizde staj yapmayı arzuluyorum.

Özellikle şirketinizdeki tecrübeli ekipten öğrenme fırsatı bulmanın, yetkinliklerimi geliştirme yolunda büyük katkı sağlayacağına inanıyorum. CV'mi ekte bulabilirsiniz. Değerlendirmeniz için teşekkür eder, uygun gördüğünüz takdirde benimle iletişime geçmenizden memnuniyet duyarım.

İyi çalışmalar,
Muhammed Kılıç
"""

# CV dosya yolu
cv_path = "/home/muhammet/Downloads/yenicv.pdf"  # CV dosyanızın bulunduğu yol

# E-posta gönderme fonksiyonu
def send_email(to_email):
    # E-posta nesnesi oluştur
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # E-posta gövdesi
    msg.attach(MIMEText(body, 'plain'))

    # CV ekle
    with open(cv_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= yenicv.pdf")
    msg.attach(part)

    # E-posta gönder
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to_email, msg.as_string())
        print(f"E-posta başarıyla gönderildi: {to_email}")
    except Exception as e:
        print(f"Hata oluştu {to_email}: {e}")
    finally:
        server.quit()

# Tüm e-posta adreslerine gönderim
with open("mailler.txt", "r") as file:
    for line in file:
        email = line.strip()
        if email:  # Boş satırları atla
            send_email(email)
            time.sleep(1)  # Her e-posta gönderiminden sonra 1 saniye bekle
