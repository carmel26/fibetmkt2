from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
