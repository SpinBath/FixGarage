from django.db import models
from django.contrib.auth.models import User

import uuid as uuid_lib
# Create your models here.



class Clients(models.Model):
        
        id = models.UUIDField(
                default=uuid_lib.uuid4,
                unique=True,
                primary_key=True,
                editable=False
        )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100)
        address = models.CharField(max_length=200)
        phone = models.CharField(max_length=15)
        email = models.EmailField()
        
        def __str__(self):
                return str(self.name +' (' + self.phone + ')')

class Vehicles(models.Model):
        
        id = models.UUIDField(
                default=uuid_lib.uuid4,
                unique=True,
                primary_key=True,
                editable=False
        )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        owner = models.ForeignKey(Clients, on_delete=models.CASCADE)
        brand = models.CharField(max_length=50)
        model = models.CharField(max_length=50)
        year = models.IntegerField()
        license_plate = models.CharField(max_length=17)

        def __str__(self):
                return str(self.brand + ' ' + self.model + ' (' + self.license_plate + ')')


class Services(models.Model):
        
        id = models.UUIDField(
                default=uuid_lib.uuid4,
                unique=True,
                primary_key=True,
                editable=False
        )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
        owner = models.ForeignKey(Clients, on_delete=models.CASCADE)
        description = models.TextField()
        entry_date = models.DateField()
        departure_date = models.DateField()
        price = models.DecimalField(max_digits=10, decimal_places=2)


class Billing(models.Model):

        id = models.UUIDField(
                default=uuid_lib.uuid4,
                unique=True,
                primary_key=True,
                editable=False
        )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
        owner = models.ForeignKey(Clients, on_delete=models.CASCADE)
        description = models.TextField()
        entry_date = models.DateField()
        departure_date = models.DateField()
        final_price = models.DecimalField(max_digits=10, decimal_places=2)
        status = models.BooleanField()
        

