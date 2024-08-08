from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #usado para listar os campos que vão aparecer no registro do carro
    search_fields = ('model','brand') #usado para escolher o que será pesquisado

admin.site.register(Car, CarAdmin) #usado para registrar no server. tem que os dois parâmetros

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)