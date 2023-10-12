from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

def account(request):
    return render(request, 'user/account.html')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'user/signin.html', {'form': form, 'errors': form.errors})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Получаем имя пользователя из формы
            username = form.cleaned_data.get('username')
            # Перенаправляем пользователя на страницу авторизации
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form, 'errors': form.errors})

def logoutView(request):
    logout(request)
    return redirect('/')

# Create your views here.
