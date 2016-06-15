from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Sujet(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Poids(models.Model):
    nom = models.CharField(max_length=250)
    poids = models.IntegerField()
    ordre = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "poids"

    def __str__(self):
        return self.nom

class Vote(models.Model):
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE)
    nom = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now, blank=True)
    poids = models.ForeignKey(Poids, on_delete=models.CASCADE)

