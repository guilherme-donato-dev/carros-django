from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

def cars_view(request):
    return HttpResponse('<h1>Meus carros top demaaaais</h1>')
