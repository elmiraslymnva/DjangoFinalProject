# Python tabanlı bir imaj kullanıyoruz
FROM python:3.8

# Çalışma dizinini belirleyelim
WORKDIR /app

# Gereksinimleri kopyalayalım
COPY requirements.txt /app/

# Gereksinimleri yükleyelim
RUN pip install --no-cache-dir -r requirements.txt

# curl'ü yükleyelim
RUN apt-get update && apt-get install -y curl

# wait-for-it betiğini indiriyoruz (RabbitMQ ve PostgreSQL'i beklemek için)
RUN curl -sSLo /usr/local/bin/wait-for-it https://github.com/vishnubob/wait-for-it/releases/download/v2.3.0/wait-for-it-linux-x86_64.sh
RUN chmod +x /usr/local/bin/wait-for-it

# Proje dosyalarını kopyalayalım
COPY . /app/

# Django için gerekli portu açalım
EXPOSE 8000

# RabbitMQ ve PostgreSQL servislerinin başlatılmasını bekleyelim
CMD /usr/local/bin/wait-for-it rabbitmq:5672 -- /usr/local/bin/wait-for-it db:5432 -- python manage.py runserver 0.0.0.0:8000

RUN apt-get update && apt-get install -y libpq-dev
