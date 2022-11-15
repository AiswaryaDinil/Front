from django.db import models
from django.contrib.auth.models import User

class Useradd(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    accounts=models.BooleanField(default=False)
    hr=models.BooleanField(default=False)
    sales=models.BooleanField(default=False)
    purchase=models.BooleanField(default=False)
    reports=models.BooleanField(default=False)
    def __str__(self):
        return self.email