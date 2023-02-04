from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=256, unique=True)
    last_name = models.CharField(max_length=256)
    major = models.CharField(max_length=256)
    dob = models.DateField()

    def __str__(self):
        return self.first_name
