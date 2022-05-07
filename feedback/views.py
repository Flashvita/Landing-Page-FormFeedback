from django.views.generic import CreateView
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from .services import send
from django.core.mail import mail_admins
from django.core.mail import send_mail




class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        new_message = form.cleaned_data
        form.save()
        send_mail('Заказ обратного звонка',
                  'Здраствуйте меня зовут {} мой номер телефона"{}" и мой email"{}"'.
                  format(new_message['name'], new_message['phone'], new_message['email']),
                  'DjangoTestemail2022@gmail.com', ['DjangoTestemail2022@gmail.com', 'Flashvita@yandex.ru'], fail_silently=False
                  )
        return super().form_valid(form)


