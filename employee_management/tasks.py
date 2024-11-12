from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def sample_task():
    print("Sample task executed!")

from celery import shared_task
from .models import Employee
from django.core.mail import send_mail

@shared_task
def send_welcome_email(employee_id):
    employee = Employee.objects.get(id=employee_id)
    send_mail(
        'Hoşgeldiniz!',
        f'{employee.first_name} {employee.last_name} hoş geldiniz!',
        'from@example.com',
        [employee.email],
        fail_silently=False,
    )

@shared_task
def example_task():
    print("Bu görev çalışıyor!")