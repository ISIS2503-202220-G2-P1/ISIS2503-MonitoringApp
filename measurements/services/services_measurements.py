from monitoring.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.core.mail import send_mail

def check_alarm(value):
    if value >= 42:
        send_email()
        send_email2()
    return()

def send_email():
    subject = 'Test Taller'
    message = 'Warning!!! the temperature is growing'
    recepient = "j.alegria@uniandes.edu.co"
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], auth_password=EMAIL_HOST_PASSWORD)

def send_email2():
    subject2 = 'Test Taller'
    message2 = 'Warning!!! the temperature is growing'
    recepient2 = "t.acosta@uniandes.edu.co"
    send_mail(subject2, message2, EMAIL_HOST_USER, [recepient2], auth_password=EMAIL_HOST_PASSWORD)    