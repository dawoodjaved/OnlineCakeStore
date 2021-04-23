from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ('Genoise Cake', 'Genoise Cake'),
    ('Angel Food Cake', 'Angel Food Cake'),
    ('Biscuit Cake', 'Biscuit Cake'),
    ('Pound Cake', 'Pound Cake'),
    ('Sponge Cake', 'Sponge Cake'),
    ('Chiffon Cake', 'Chiffon Cake'),
    ('Baked Flourless Cake', 'Baked Flourless Cake'),
    ('Carrot Cake', 'Carrot Cake'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'
