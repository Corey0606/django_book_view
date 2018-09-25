from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 与Publish表建立一对多的关系 ，外键字段在多的一方
    publish = models.ForeignKey(to='Publish', to_field='nid', on_delete=models.CASCADE)
    # 与Author建立多对多的关系
    author = models.ManyToManyField(to='Author')


