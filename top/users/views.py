from django.shortcuts import render, redirect
from .models import *  # импортирование модели


# from .models import Users


def log_in(request):
    # users = Users.objects.all()  # запрос в базу данных
    return render(request, 'log_in.html', {})  # отправка в html


def register(request):
    # registers = Users.objects.all()  # запрос в базу данных
    return render(request, 'register.html', {})  # отправка в html
