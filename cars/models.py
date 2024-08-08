from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta: ordering = ('name',)
    #para substituir o "Car Object" e aparecer o nome da própria marca quando clicar nele
    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(null=True, blank=True)
    model_year = models.IntegerField(null=True, blank=True)
    plate = models.CharField(max_length=10, null=True, blank=True)
    value = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='cars/', null=True, blank=True)

    #para substituir o "Car Object" e aparecer o nome do próprio carro quando clicar nele
    def __str__(self):
        return self.model
    
