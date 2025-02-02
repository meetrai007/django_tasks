from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    class_name = models.CharField(max_length=100,choices=(('11th','11th'),('12th','12th'))) # Add choices 11th, 12th
    city = models.CharField(max_length=100)