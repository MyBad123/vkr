from django.shortcuts import render, redirect
from .models import MailModel

from django.conf import settings
from django.conf.urls.static import static

def get_main(request):
    """get main page"""

    return render(request, 'index.html')


def set_mail(request):
    """set mail"""

    # get mail
    mail = request.POST.get('mail', None)
    if (mail == None) or (mail == ''):
        return redirect('/app/main')

    if '@' in mail:
        MailModel.objects.create(
            mail=mail
        )

    return redirect('/app/main')
