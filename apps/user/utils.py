from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(subject, message, to_email):
        email = EmailMessage(to=[to_email], subject=subject, body=message)
        email.send()
