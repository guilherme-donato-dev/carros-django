from django.db import models

# Create your models here.
#depois de mexer no models sempre dê o makemigrations e migrate

#criação da tabela Brand com os atributos/colunas logo abaixo
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta: ordering = ('name',)
    #para substituir o "Car Object" e aparecer o nome da própria marca quando clicar nele
    def __str__(self):
        return self.name


#criação da tabela Car com os atributos/colunas logo abaixo
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    color = models.CharField(max_length=40, null=True, blank=True )
    factory_year = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    plate = models.CharField(max_length=10, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='cars/', null=True, blank=False)
    bio = models.TextField(blank=True, null=True)

    #para substituir o "Car Object" e aparecer o nome do próprio carro quando clicar nele
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-created_at'] #para ordenar o created_at de forma decrescente.

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'