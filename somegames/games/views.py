from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'Strona Główna',
    }
    if request.user.is_authenticated:
        retcode = 200
        return render(request, 'games/home.html', context, status=retcode)
    else:
        messages.info(request, "Zaloguj się, by wejść na stronę")
        return redirect('login')


def login_user(request):
    context = {
        'title': 'Logowanie',
        'form': LoginForm(),
    }
    if request.user.is_authenticated:
        messages.info(request, "Już jesteś zalogowany/a.")
        return redirect('home')
    else:
        retcode = 200
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
            
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Zalogowano pomyślnie.")
                    return redirect('home')
                else:
                    messages.error(request, "Nieprawidłowy login lub hasło. Spróbuj ponownie.")
                    return redirect('login')
            else:
                return HttpResponse('Invalid')
        else:
            return render(request, 'games/login.html', context, status=retcode)


def logout_user(request):
    logout(request)
    messages.success(request, "Pomyślnie wylogowano.")
    return redirect('login')


def register_user(request):
    context = {
        'title': 'Rejestracja',
        'form': RegisterForm(),
    }
    if request.user.is_authenticated:
        messages.info(request, "Już jesteś zalogowany/a.")
        return redirect('home')
    else:
        retcode = 200
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Zarejestrowano pomyślnie.")
                return redirect('login')
            else:
                messages.error(request, "Niepoprawny formularz.")
        return render(request, 'games/register.html', context, status=retcode)


def all_games(request):
    context = {
        'title': 'Gry',
    }
    if request.user.is_authenticated:
        retcode = 200
        return render(request, 'games/all_games.html', context, status=retcode)
    else:
        messages.info(request, "Zaloguj się, by wejść na stronę")
        return redirect('login')
        


def profile(request):
    context = {
        'title': f'Profil: {request.user.username}',
    }
    if request.user.is_authenticated:
        retcode = 200
        return render(request, 'games/profile.html', context, status=retcode)
    else:
        messages.info(request, "Zaloguj się, by wejść na stronę")
        return redirect('login')


def settings(request):
    context = {
        'title': 'Ustawienia',
    }
    if request.user.is_authenticated:
        retcode = 200
        return render(request, 'games/settings.html', context, status=retcode)
    else:
        messages.info(request, "Zaloguj się, by wejść na stronę")
        return redirect('login')