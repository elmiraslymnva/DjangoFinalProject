import time
import os
import socket

# RabbitMQ ve PostgreSQL için host ve port bilgileri
RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
POSTGRES_HOST = 'db'
POSTGRES_PORT = 5432

# RabbitMQ ve PostgreSQL servislerinin çalışmaya başlamasını beklemek için bir fonksiyon
def wait_for_service(host, port, retries=10):
    for i in range(retries):
        try:
            with socket.create_connection((host, port), timeout=5):
                print(f"{host}:{port} is ready!")
                return True
        except (socket.timeout, socket.error):
            print(f"Waiting for {host}:{port} to be ready... Attempt {i+1}/{retries}")
            time.sleep(5)
    return False

# RabbitMQ ve PostgreSQL servislerinin hazır olmasını bekleyelim
if wait_for_service(RABBITMQ_HOST, RABBITMQ_PORT) and wait_for_service(POSTGRES_HOST, POSTGRES_PORT):
    print("All services are ready. Starting Django server.")
    os.system('python manage.py runserver 0.0.0.0:8000')
else:
    print("Services did not start in time.")
