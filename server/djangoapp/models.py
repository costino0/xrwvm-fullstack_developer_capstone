# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique name for the car make
    description = models.TextField(blank=True)  # Optional description
    country_of_origin = models.CharField(max_length=100, blank=True)  # Country where the make is based
    founded_year = models.PositiveIntegerField(null=True, blank=True)  # Year the make was founded
    logo = models.ImageField(upload_to='car_makes/logos/', blank=True, null=True)  # Optional logo image

    def __str__(self):
        return self.name  # Return the name as the string representation


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    country_of_origin = models.CharField(max_length=100, blank=True)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to='car_makes/logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField()  # Dealer ID referring to a dealer in Cloudant database
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),  # Adjust this to the current year as needed
            MinValueValidator(2015)
        ]
    )

    # Additional fields can be added here
    color = models.CharField(max_length=30, blank=True)  # Optional field for car color
    mileage = models.PositiveIntegerField(null=True, blank=True)  # Optional field for mileage

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Return a string representation of the car make and model