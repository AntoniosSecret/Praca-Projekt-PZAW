from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages



def home(request):
    context = {
        'title': 'Home'
    }
    if request.user.is_authenticated:
        retcode = 200
        return render(request, 'games/home.html', context, status=retcode)
    else:
        retcode = 400
        return redirect('login')


def login_user(request):
    context = {
        'title': 'Login'
    }
    if request.user.is_authenticated:
        retcode = 400
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


def all_games(request):
    retcode = 200
    context = {}
    return render(request, 'games/all_games.html', context, status=retcode)