from django.db import models


class Catalog(models.Model):
    nombre_catalog = models.CharField(max_length=40)
    description = models.CharField(max_length=120)
    #especie = models.CharField(max_length=25)
    #genero = models.CharField(max_length=1)