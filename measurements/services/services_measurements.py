from monitoring.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.core.mail import send_mail

def check_alarm(value):
    if value >= 42:
        send_email()

    return()

def send_email():
    subject = 'Test Taller'
    message = 'Warning!!! the temperature is growing'
    recepient_a = "j.alegria@uniandes.edu.co"
    recipient_b = "t.acosta@uniandes.edu.co"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient_a, recipient_b], auth_password=EMAIL_HOST_PASSWORD)
   