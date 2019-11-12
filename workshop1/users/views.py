import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings

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