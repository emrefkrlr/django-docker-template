# Django + Docker Professional Starter Template

**Bu proje;** Docker üzerinde koşan, PostgreSQL veritabanı kullanan, Custom User Model (Özel Kullanıcı Modeli) ve *django-allauth* (Google OAuth dahil) entegrasyonu tamamlanmış profesyonel bir başlangıç şablonudur.

## 🚀 Özellikler
- Dockerize Yapı: docker-compose ile tek komutla geliştirme ve deploy ortamı.

- **Custom User Model:** Projenin başında özelleştirilebilir kullanıcı tablosu (users.User).

- **Django-Allauth:** E-posta/Şifre ve Sosyal medya (Google) ile giriş desteği.

- **PostgreSQL:** Veritabanı olarak güvenilir ve performanslı Postgres 16.

- **Gelişmiş Ortam Yönetimi:** .env dosyası üzerinden dinamik yapılandırma.

- **Proxy Hazırlığı:** Üretim (Production) ortamı için Nginx proxy yapılandırması hazır.

## 🛠️ Hızlı Kurulum
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
