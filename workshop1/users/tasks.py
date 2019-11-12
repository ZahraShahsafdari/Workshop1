from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep
from users.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import uuid

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def signup(request):
    sleepy.delay(3)
    if request.method == 'GET':
        return render(
            request,
            'signup.html',
            context = { }
        )
    elif request.method == 'POST':
        u = User(
            first_name = request.POST['firstname'],
            last_name = request.POST['lastname'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        u.set_password(request.POST['password'])
        u.token = uuid.uuid4()
        u.save()

        #for verifying email
        subject = 'Thank you for registering to our site'
        message = ' it means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        msg_html = render_to_string('email.html')   
        send_mail( subject, message, email_from, recipient_list, html_message = msg_html)
    return HttpResponse('Successfully joined! Please check your email for verification.')