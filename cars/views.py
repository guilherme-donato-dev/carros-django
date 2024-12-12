from typing import Any
from django.db.models.query import QuerySet
from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator #Em Django, um decorator é uma função que permite modificar o comportamento de outra função ou método, geralmente de forma reutilizável e concisa. Eles são frequentemente usados para modificar ou estender a funcionalidade de views ou de outros métodos dentro de um projeto Django.
from django.contrib.auth.decorators import login_required #login_required é um decorator nativo de Django, que faz com que o usuário so consiga realizar algumas funções com o login.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView #todos nativos do django

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
    

@method_decorator(login_required(login_url= 'login'), name= 'dispatch')
class NewCarCreateView(CreateView):  #como é CreateView, o django automaticamente já sabe que vai chegar get e post, e ele reconhece isso, então eu nao preciso passar a função de quando for get e quando for post. No GET ele vai renderizar o new_car.html e no post ele vai enviar o novo carro para o BD.
    model = Car
    form_class = CarModelForm #literalmente qual estilo de form você quer usar
    template_name = 'new_car.html' #qual template que utilizo
    success_url = '/cars/' #aqui ele pede qual url eu devo enviar o carro depois de cadastrar, que nesse caso é cars_list


class CarDetailView(DetailView):  #view nativa de Django 
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url= 'login'), name= 'dispatch') 
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk' : self.object.pk})
    
    
@method_decorator(login_required(login_url= 'login'), name= 'dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'