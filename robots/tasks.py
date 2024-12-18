from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from django.core import mail


@shared_task
def send_message_to_customer(robot_model, robot_version, email):
    subject = "Ваш заказ готов!"
    body = (
        "Добрый день!\n"
        f"Недавно вы интересовались нашим роботом модели {robot_model}, версии {robot_version}."
        "\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"
    )

    connection = mail.get_connection()
    connection.open()

    email_message = mail.EmailMessage(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email],
        connection=connection,
    )
    email_message.send()
    connection.close()
   