from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    retcode = 200
    context = {}
    return render(request, 'games/base.html', context, status=retcode)