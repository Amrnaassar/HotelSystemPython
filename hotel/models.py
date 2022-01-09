from django.contrib.admin import options
from django.db import models

# Create your models here.
class booking (models.Model):

    name=models.CharField(max_length=100)
    id=models.IntegerField(name='ID',primary_key=True)
    days=models.IntegerField(name='days')
    roomnum=models.IntegerField(name='roomnum')
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class room(models.Model):
    number=models.IntegerField(name='number',primary_key=True)
    type =models.CharField(max_length=100)
    price =models.IntegerField(name='price')


