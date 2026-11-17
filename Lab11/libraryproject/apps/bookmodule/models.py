from django.db import models

class Book(models.Model): 
    title = models.CharField(max_length = 50) 
    author = models.CharField(max_length = 50) 
    price = models.FloatField(default = 0.0) 
    edition = models.SmallIntegerField(default = 1) 


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    image = models.FileField(upload_to='flowers/')

    def __str__(self):
        return self.name

