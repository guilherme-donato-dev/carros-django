from django.db.models.signals import    pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value') #SUM é igual ao SUM de SQL,ele soma todos os valores de value.
    )['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )


@receiver(post_save, sender=Car ) #o receiver é basicamente uma função que fica "ouvindo" os eventosque estão chegando, e o sender é o Model
def car_post_save(sender, instance, **kwargs):  #sender é o model que tá enviando o evento
    car_inventory_update()


@receiver(post_delete, sender=Car) 
def car_post_delete(sender, instance, **kwargs): 
    car_inventory_update()