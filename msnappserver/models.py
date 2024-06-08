from django.db import models


class User1(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class News1(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField(max_length=100)
    photoURL = models.CharField(max_length=200)
    likes = models.IntegerField()
