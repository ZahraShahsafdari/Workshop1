from django.urls import path
from . import views
from . import tasks

urlpatterns = [
    path('signup', views.signup),
    path('login', views.loginview),
    path('login/list', views.loginview),
    ]