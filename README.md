# django-docker-template


## Projeyi Kurmak

- Docker Kurulu Olması Gerekiyor
- Projeji çalışma ortamınıza indirin
-- git clone https://github.com/emrefkrlr/django-docker-template.git
- docker-compose build
- docker-compose up
- Admin için super user oluştur
    docker-compose run --rm app sh -c "python manage.py createsuperuser"

Geliştirme ortamında localhost:8000 portunda çalıştırabilirsin

Projeni canlıya almadan önce test etmek için

- docker-compose -f docker-compose-deploy.yml down --volumes
- docker-compose -f docker-compose-deploy.yml build
- docker-compose -f docker-compose-deploy.yml up
- docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"



