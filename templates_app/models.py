from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    bio = models.TextField()
    bith_date = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
    

class Product(models.Model):
    name = models.CharField(max_length=122)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    in_stock = models.BooleanField()


    def __str__(self):
        return f'{self.name}'

