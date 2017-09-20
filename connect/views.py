# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail

from .forms import ConnectForm
from django.shortcuts import render


def connect(request):
    form = ConnectForm(request.POST or None)
    if form.is_valid():
        form.save()
        form_email = form.cleaned_data.get("email")
        subject = 'Thanks for connecting'
        form_name = form.cleaned_data.get("name")
        thankyou_msg = '''Hi %s, \n\n Thanks for connecting. \n I will respond to you at the earliest.\n\nThanks, \n Siva Reddy  ''' %(form_name)
        from_email = settings.EMAIL_HOST_USER
        to_email = [form_email,]
        send_mail(subject, thankyou_msg, from_email, to_email, fail_silently= False)
        form = ConnectForm()
    return render(request, "connect/connect.html", {'form': form})
