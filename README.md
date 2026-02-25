# Django + Docker Professional Starter Template

**Bu proje;** Docker üzerinde koşan, PostgreSQL veritabanı kullanan, Custom User Model (Özel Kullanıcı Modeli) ve *django-allauth* (Google OAuth dahil) entegrasyonu tamamlanmış profesyonel bir başlangıç şablonudur.

## 🚀 Özellikler
- Dockerize Yapı: docker-compose ile tek komutla geliştirme ve deploy ortamı.

- **Custom User Model:** Projenin başında özelleştirilebilir kullanıcı tablosu (users.User).

- **Django-Allauth:** E-posta/Şifre ve Sosyal medya (Google) ile giriş desteği.

- **PostgreSQL:** Veritabanı olarak güvenilir ve performanslı Postgres 16.

- **Gelişmiş Ortam Yönetimi:** .env dosyası üzerinden dinamik yapılandırma.

- **Proxy Hazırlığı:** Üretim (Production) ortamı için Nginx proxy yapılandırması hazır.

* **Dinamik Format Dönüştürme:** Tüm resimler otomatik olarak **WebP** ve **AVIF** formatlarında sunulur.
* **On-the-fly Boyutlandırma:** Template içinden istenilen her boyutta resim üretilebilir (örn: 300x200, 800x600).
* **Akıllı Watermark:** * Resim boyutuna göre otomatik ölçeklenen dinamik font boyutu.
    * Merkezi konumlandırma ve ayarlanabilir şeffaflık.
    * `.env` üzerinden açılıp kapatılabilme özelliği.
* **Performans:** Üretilen resimler `media/CACHE/` altında saklanır, tekrar tekrar işlenmez.

* **Multi-Language (i18n):** TR/EN support with prefix-less default language.

* **Dynamic Menus:** Database-driven header and footer menus with external URL support.

* **System Dashboard:** A stylish index.html to monitor system status and test all features.


## 🖼️ Gelişmiş Resim İşleme ve SEO Yönetimi
Bu template, görsel içeriklerin hem SEO performansını artırmak hem de sunucu kaynaklarını verimli kullanmak için Django-ImageKit, Pillow-Heif ve özel geliştirilmiş bir Watermark Service ile entegre gelir.

### 🌟 Öne Çıkan Özellikler
- Dinamik Format Dönüşümü: Orijinal resim ne olursa olsun (JPG, PNG), sistem bunları otomatik olarak modern WebP ve AVIF formatlarına dönüştürür.

- On-the-Fly (Anlık) Boyutlandırma: Modellerde onlarca farklı boyut tanımlamanıza gerek kalmaz. Boyutlandırma doğrudan template (HTML) üzerinden yönetilir.

- Akıllı Watermark Sistemi:

- Resim boyutuna göre %12 oranında dinamik ölçeklenen yazı boyutu.

- Yüksek çözünürlüklü resimlerde bile net okunan Bold (Kalın) font desteği.
- Merkezi konumlandırma ve %60 şeffaflık ile profesyonel görünüm.

- Performans & Cache: İşlenen resimler media/CACHE/ dizininde saklanır. Bir resim sadece bir kez işlenir ve sonraki isteklerde cache'den sunulur.

## ⚙️ Yapılandırma
Watermark özelliğini ortam değişkenleri üzerinden kolayca yönetebilirsiniz:

**docker-compose.yml veya .env:**
```python
environment:
  - WATERMARK_ENABLED=True  # Watermark'ı açar (True) veya kapatır (False)
```

## 🚀 Kullanım Rehberi
### 1. Model Yapısı
Herhangi bir modelde ImageField veya FileField kullanmanız yeterlidir. save() metodunda apply_watermark fonksiyonunu çağırmak, yüklenen orijinal resmi otomatik olarak mühürler.

```python
# core/models.py
from .image_service import apply_watermark

class Sample(models.Model):
    attachment = models.ImageField(upload_to='samples/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.attachment:
            apply_watermark(self.attachment.path)

```

### 2. Template (HTML) İçinde Kullanım
Resimleri farklı boyutlarda ve modern formatlarda çağırmak için core:seo_image jeneratörünü kullanın:

```html
{% load imagekit %}

<picture>
    {# AVIF Versiyonu (En yüksek sıkıştırma) #}
    {% generateimage 'core:seo_image' source=obj.attachment width=800 height=600 format='AVIF' as img_avif %}
    <source srcset="{{ img_avif.url }}" type="image/avif">

    {# WebP Versiyonu (Yüksek uyumluluk) #}
    {% generateimage 'core:seo_image' source=obj.attachment width=800 height=600 format='WEBP' as img_webp %}
    <source srcset="{{ img_webp.url }}" type="image/webp">

    {# Fallback (Orijinal resim) #}
    <img src="{{ obj.attachment.url }}" alt="Açıklama" width="800" height="600">
</picture>
````

## 🛠️ Teknik Gereksinimler
Bu sistemin çalışması için requirements.txt dosyasında aşağıdaki paketler tanımlıdır:

- **django-imagekit:** Dinamik işleme için.

- **pillow-heif:** AVIF yazma desteği için.

- **Pillow:** Temel görüntü işleme için.


## 🛠️ Proje Hızlı Kurulum
Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Projeyi Klonlayın

```python
git clone https://github.com/emrefkrlr/django-docker-template.git
````

### 2. Ortam Değişkenlerini Ayarlayın
**.env.sample** dosyasını **.env** adıyla kopyalayın ve içindeki değerleri kendinize göre güncelleyin:

```bash
cp .env.sample .env
````

### 3. Ortamı Ayağa Kaldırma ve başlatma
```bash
docker compose up -d --build
```


Bu komut; veritabanını oluşturur, migration'ları yapar ve web sunucusunu http://localhost:8000 adresinde başlatır.

## 🔑 Sosyal Giriş (Google OAuth) Kurulumu
- Google ile girişi aktif etmek için:

- Google Cloud Console üzerinden bir proje oluşturun.

- OAuth 2.0 Client ID oluşturun ve Redirect URI olarak http://localhost:8000/accounts/google/login/callback/ adresini ekleyin.

- Aldığınız Client ID ve Secret bilgilerini .env dosyanızdaki şu alanlara yapıştırın:

```text
GOOGLE_CLIENT_ID=your-id
GOOGLE_SECRET=your-secret
````

- Konteynerları yeniden başlatmanıza gerek kalmadan sistem bu bilgileri okuyacaktır.

## 📁 Proje Yapısı

- ***/app:*** Django kaynak kodları.

- ***/users:*** Özel kullanıcı modeli ve kimlik doğrulama işlemleri.

- ***/config:*** Django ayarlarının bulunduğu ana klasör.

- ***/proxy:*** (Üretim ortamı için) Nginx konfigürasyonu.

- ***docker-compose.yml:*** Geliştirme (Local) yapılandırması.

- ***docker-compose-deploy.yml:*** Yayına alım (Production) yapılandırması.

## 🧪 Faydalı Komutlar

### Superuser Oluşturma:

```bash
docker-compose exec app python manage.py createsuperuser
```

### Logları İzleme:

```bash
docker-compose logs -f
```

### Yeni Migration Oluşturma:

```bash
docker-compose exec app python manage.py makemigrations
```

## 📝 Notlar
- Geliştirme aşamasında DEBUG=1 olduğundan emin olun.

- Üretim ortamına geçerken docker-compose-deploy.yml kullanın ve DEBUG=0 yapın.

- Projeni canlıya almadan önce test etmek için:

```
docker-compose -f docker-compose-deploy.yml down --volumes
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up
docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"
```
