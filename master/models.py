from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=320)  # TODO Change database definition documentation
    email = models.CharField(max_length=40)


class Category(models.Model):
    name = models.CharField(max_length=25)


class Offers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()


class Messages(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE)
