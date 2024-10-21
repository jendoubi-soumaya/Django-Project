from django import forms
from .models import Annonce

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre', 'localisation', 'category', 'prix', 'description', 'nombre_de_chambres', 'equipe', 'surface', 'images']
