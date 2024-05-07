
from django.db import models

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)  # the password is the same as matricule
    
    def __str__(self):
        return self.full_name
