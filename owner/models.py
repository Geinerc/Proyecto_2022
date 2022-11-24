from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    pais = models.CharField(max_length=120, default='coño')