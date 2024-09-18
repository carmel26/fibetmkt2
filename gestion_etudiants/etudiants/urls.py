from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('liste/', views.liste_etudiants, name='liste_etudiants'),
    path('modifier/<int:id>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('supprimer/<int:id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('voir/<int:id>/', views.voir_etudiant, name='voir_etudiant'),  # Ajoutez cette ligne
]
