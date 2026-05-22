from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(2000)])

    def __str__(self):
        return self.name
    
