from django.shortcuts import render
from cars.models import Car

# Create your views here.


# Create your views here.

def cars_view(request):
    print(request.GET)

    print(request.GET.get('search'))

    cars = Car.objects.filter(model__contains='Cobalt')


    return render(
        request, 
        'cars.html',
        {'cars' : cars}
        )
