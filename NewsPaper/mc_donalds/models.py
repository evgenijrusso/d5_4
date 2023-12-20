

from django.db import models
from django.utils import timezone

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]


class Order(models.Model):  # Заказ
    time_in = models.DateTimeField(default=timezone.now)                         #(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=9.0)  # стоимость
    pickup = models.BooleanField(default=False)  # самовывоза (True) или доставка(False)
    complete = models.BooleanField(default=False) # Заказ уже выполнен
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField('Product', through='ProductOrder')


class Staff(models.Model):  # штат
    full_name = models.CharField(max_length=250)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)      # должность
    labor_contract = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    composition = models.TextField(default="Состав не указан")


class ProductOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=1)  # кол-во продуктов в заказе

'''
Добавил для полей order, product, staff (все внешние ключи) опции  null=True, blank=True. Причина: миграция не 
может создать пустое поле. Без этих опций пришлось бы удалять все миграции и создаваать их заново (и чистить БД)
Так же изменил опцию  (auto_now_add=True) на timezone.now. Примерно такая же причина  
'''