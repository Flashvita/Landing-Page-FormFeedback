from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'У вас новый клиент',
        'Здраствуйте меня зовут {} мой номмер телефона {}',
        [user_email],
        'DjangoTestemail2022@gmail.com',
        fail_silently=False,
    )
