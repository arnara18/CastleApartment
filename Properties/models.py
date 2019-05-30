from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Types(models.Model):
    type = models.CharField(max_length=50)


class Cities(models.Model):
    country = models.CharField(max_length=999)
    city = models.CharField(max_length=150)
    zip = models.IntegerField()


class Addresses(models.Model):
    street = models.CharField(max_length=150)
    house_number = models.IntegerField()
    cites_id = models.ForeignKey(Cities, on_delete=models.DO_NOTHING)


class Rooms(models.Model):
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    living_rooms = models.IntegerField()


class Tags(models.Model):
    elevator = models.BooleanField()
    garage = models.BooleanField()


class Details(models.Model):
    size = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    type = models.ForeignKey(Types, on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)


class Properties(models.Model):
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    details = models.ForeignKey(Details, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
