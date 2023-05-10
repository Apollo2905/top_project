from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# from .models import Users

# AnonymousUser - статус неавторизованного пользователя

def log_in(request):
    valid_user = True
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:home')
        valid_user = False
    form = AuthenticationForm()
    return render(request, 'log_in.html', {'form': form, 'valid_user': valid_user})  # отправка в html


def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:log_in')
    return render(request, 'register.html', {'form': form})  # отправка в html


def log_out(request):
    logout(request)
    return redirect('users:log_in')
