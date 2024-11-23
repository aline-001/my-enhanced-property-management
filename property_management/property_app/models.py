from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


property_type=[
    ('apartment', 'Apartment'),
    ('house', 'House'),
    ('commercial', 'Commercial'),
    ("Land", "Land"),
]


class Property(models.Model):
    name = models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    type=models.CharField(max_length=20, choices=property_type)
    description=models.TextField(max_length=200)
    number_of_units=models.IntegerField()

    def __str__(self):
        return self.name


class Units(models.Model):
    property=models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number=models.CharField(max_length=100)
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    rent=models.IntegerField()
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.unit_number} -- {self.property.name}"


class Tenant(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Lease(models.Model):
    tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit=models.ForeignKey(Units, on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    rent_amount=models.IntegerField()

    def __str__(self):
        return f"{self.tenant.name}'s lease"
