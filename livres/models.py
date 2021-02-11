from django.db import models


class Livre(models.Model):
    titre = models.CharField(max_length=100)
    datePub = models.CharField(max_length=100)
    description = models.TextField(null=True)
    auteur = models.ForeignKey(
        "Auteur",
        related_name="livres",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    dateNais = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
