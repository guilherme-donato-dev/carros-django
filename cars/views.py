from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cars_view(request):
    return HttpResponse('<h1>Meus carros valeu sapo</h1>')