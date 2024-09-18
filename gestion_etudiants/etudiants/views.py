from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant, Departement
from .forms import EtudiantForm, DepartementForm


def voir_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, pk=id)
    return render(request, 'etudiants/voir_etudiant.html', {'etudiant': etudiant})


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste_etudiants.html', {'etudiants': etudiants})

def ajouter_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/ajouter_etudiant.html', {'form': form})

def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, pk=id)
    
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    
    return render(request, 'etudiants/modifier_etudiant.html', {'form': form, 'etudiant': etudiant})

def modifier_etudiant1(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/modifier_etudiant.html', {'form': form})

def supprimer_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == "POST":
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'etudiants/supprimer_etudiant.html', {'etudiant': etudiant})
