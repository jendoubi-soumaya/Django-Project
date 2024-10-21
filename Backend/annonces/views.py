from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Annonce
from .forms import AnnonceForm

def create_annonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('annonce_list')
    else:
        form = AnnonceForm()
    return render(request, 'annonces/create_annonce.html', {'form': form})

def annonce_list(request):
    annonces = Annonce.objects.all()
    return render(request, 'annonces/annonce_list.html', {'annonces': annonces})

def update_annonce(request, pk):
    annonce = Annonce.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnnonceForm(request.POST, request.FILES, instance=annonce)
        if form.is_valid():
            form.save()
            return redirect('annonce_list')
    else:
        form = AnnonceForm(instance=annonce)
    return render(request, 'annonces/update_annonce.html', {'form': form})

def delete_annonce(request, pk):
    annonce = Annonce.objects.get(pk=pk)
    if request.method == 'POST':
        annonce.delete()
        return redirect('annonce_list')
    return render(request, 'annonces/delete_annonce.html', {'annonce': annonce})
