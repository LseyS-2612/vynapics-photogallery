# 1. Resmi ve hafif bir Python altyapısı kullanıyoruz
FROM python:3.11-slim

# 2. Konteyner içinde çalışma klasörünü oluştur
WORKDIR /app

# 3. Önce gereksinim dosyasını kopyala ve kütüphaneleri kur
# (Bunu ayrı yapıyoruz ki kod değişse bile kütüphaneler tekrar tekrar yüklenmesin, cache kullansın)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kalan tüm proje dosyalarını kopyala
COPY . .

# 5. Django'nun çalışacağı 8000 portunu dış dünyaya aç
EXPOSE 8000

# 6. Konteyner başlatıldığında çalışacak komut (Sunucuyu başlat)
# 0.0.0.0 adresi Docker içinde çalışması için zorunludur.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]