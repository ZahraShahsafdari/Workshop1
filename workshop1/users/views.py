import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def signup(request):
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


def loginview(request):
    if request.method == 'GET':
        return render(
            request,
            'login.html',
            context = { }
        )
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            passwoord = request.POST['password']
        )

        # if user is not None: 
        #     login(request, user)
    users = User.objects.all()
    return render(
        request,
        'list.html',
        context = {
            'users': users,
    }
)


