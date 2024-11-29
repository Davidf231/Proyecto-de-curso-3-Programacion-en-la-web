from django.db import models

class Shinigami(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    bankai = models.CharField(max_length=60)
    escuadron = models.IntegerField()
    cargo = models.CharField(max_length=50)