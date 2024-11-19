from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

# Create your views here.


# Create your views here.

def cars_view(request):
    cars = Car.objects.all().order_by('value') #eu chamo todos os carros do meu banco de dados, a variável cars é uma query set comtodosos carros
    search = request.GET.get('search') #aqui eu guardo a busca dele na variável search

    if search: #se o user mandou uma busca, ele vai filtrar, se nao, passa direto e mostra todos
        cars = cars.filter(model__icontains = search).order_by('model')


    return render(
        request, 
        'cars.html',
        {'cars' : cars}
        )

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES) #se o método for post, ele vai enviar pro banco de dados, se for GET,que é o else, ele so carrega a paginaem branco
        if new_car_form.is_valid(): #fazendo a validação dos dados. is_valid é para checar a validação se estão corretas, as validações estão no forms.py
            new_car_form.save()
            return redirect('cars_list')  
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form' : new_car_form }
    )