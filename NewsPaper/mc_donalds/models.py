from django.db import models
from django.utils import timezone

class Order(models.Model):  # Заказ
    time_in = models.DateTimeField(default=timezone.now)  #(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=9.0)  # стоимость
    pickup = models.BooleanField(default=False)  # самовывоза (True) или доставка(False)
    complete = models.BooleanField(default=False) # Заказ уже выполнен
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, null=True, blank=True) # add related_name='order'
    products = models.ManyToManyField('Product', through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return (self.time_out-self.time_in).total_seconds()
        else:
            return (datetime.now()- self.time_in).total_seconds()  # USE_TZ=false  временно
class Staff(models.Model):  # штат

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
#   ------------------ тестовая модель с данными ---------------------------

class Country(models.Model):
     name = models.CharField(blank = True, max_length=200)
     classifier = models.CharField(blank = True, max_length=10)
     name_en = models.CharField(blank = True, max_length=200)
     name_ru = models.CharField(blank=True, max_length=200)


TYPES = [
    (news, 'Новости'),
    (articles, 'Статьи')
]

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False)
    comment_time_in = models.DateTimeField(timezone.now)
    comment_rate = models.IntegerField(default=0)