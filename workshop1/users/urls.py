from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.loginview),
    path('login/list', views.loginview),
    #path('<str:token>', views.verify),
    ]