from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

# Create your views here.


# Create your views here.

def cars_view(request):
    cars = Car.objects.all().order_by('brand','model') #eu chamo todos os carros do meu banco de dados, a variável cars é uma query set comtodosos carros
    search = request.GET.get('search') #aqui eu guardo a busca dele na variável search

    if search: #se o user mandou uma busca, ele vai filtrar, se nao, passa direto e mostra todos
        cars = cars.filter(model__icontains = search).order_by('model')


    return render(
        request, 
        'cars.html',
        {'cars' : cars}
        )

def new_car_view(request):
    new_car_form = CarForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form' : new_car_form }
    )