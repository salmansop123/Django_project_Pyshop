from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField()
    stock = models.CharField()
    image_url = models.CharField(max_length=2083) #This is industry standard for url


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField("Product Discount 20 percent", max_length=255)
    discount = models.FloatField()