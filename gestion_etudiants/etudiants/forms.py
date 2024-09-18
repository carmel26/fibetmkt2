from django import forms
from .models import Etudiant, Departement

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'departement']

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom']
