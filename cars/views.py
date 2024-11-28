from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView #todos nativos do django

# Create your views here.


# Create your views here.

    
class CarsListView(ListView):  #class based view
    model = Car #aqui eu aponto pro django qual o model que ele deve usar
    template_name = 'cars.html' #aqui estou falando qual o template que ele deve usar
    context_object_name = 'cars' 

    def get_queryset(self):  #a ListView tem um método padrão para filtrar/procurar que é o metodo get queryset
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains = search)
        return cars
    

class NewCarCreateView(CreateView):  #como é CreateView, o django automaticamente já sabe que vai chegar get e post, e ele reconhece isso, então eu nao preciso passar a função de quando for get e quando for post. No GET ele vai renderizar o new_car.html e no post ele vai enviar o novo carro para o BD.
    model = Car
    form_class = CarModelForm #literalmente qual estilo de form você quer usar
    template_name = 'new_car.html' #qual template que utilizo
    success_url = '/cars/' #aqui ele pede qual url eu devo enviar o carro depois de cadastrar, que nesse caso é cars_list