from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_mail_for_reset(request, email, new_password):
    current_site = get_current_site(request)
    context = {
        'domain': current_site.domain,
        'new_password': new_password
    }
    message = render_to_string('users/reset_email.html', context=context)
    email = EmailMessage(
        'Восстановление пароля',
        message,
        to=[email],
    )
    email.send()
