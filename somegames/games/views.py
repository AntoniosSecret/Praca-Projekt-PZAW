from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def home(request):
    context = {
        'title': 'Strona Główna'
    }
    if request.user.is_authenticated:
        retcode = 200
        return render(request, 'games/home.html', context, status=retcode)
    else:
        retcode = 400
        messages.info(request, "Zaloguj się, by wejść na stronę")
        return redirect('login')


def login_user(request):
    context = {
        'title': 'Logowanie',
        'form': LoginForm(),
    }
    if request.user.is_authenticated:
        retcode = 400
        messages.info(request, "Już jesteś zalogowany/a.")
        return redirect('home')
    else:
        retcode = 200
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Zalogowano pomyślnie.")
                return redirect('home')
            else:
                retcode = 401
                messages.error(request, "Nieprawidłowy login lub hasło. Spróbuj ponownie.")
                return redirect('login')
        else:
            return render(request, 'games/login.html', context, status=retcode)


def logout_user(request):
    logout(request)
    messages.success(request, "Pomyślnie wylogowano.")
    return redirect('login')


def register_user(request):
    retcode = 200
    context = {
        'title': 'Rejestracja'
    }
    return render(request, 'games/register.html', context, status=retcode)


def all_games(request):
    retcode = 200
    context = {}
    return render(request, 'games/all_games.html', context, status=retcode)