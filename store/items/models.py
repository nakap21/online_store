from django.db import models

# Create your models here.

class Item(models.Model):
    code = models.IntegerField(verbose_name='Code', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=200)
    category = models.CharField(verbose_name='Category', max_length=50)