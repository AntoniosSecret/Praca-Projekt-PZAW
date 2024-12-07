from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    retcode = 200
    context = {
        'title': 'Home'
    }
    return render(request, 'games/home.html', context, status=retcode)