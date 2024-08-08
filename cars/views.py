from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse

# Create your views here.

def cars_view(request):
    return HttpResponse('<h1>Meus carros valeu sapo</h1>')
>>>>>>> 8c09817 (adicionada a página cars na url)
