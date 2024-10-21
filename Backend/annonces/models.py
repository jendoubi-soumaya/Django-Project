from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Annonce(models.Model):
    CATEGORY_CHOICES = [
        ('vente', 'Vente'),
        ('location', 'Location'),
    ]

    titre = models.CharField(max_length=200)
    localisation = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    nombre_de_chambres = models.IntegerField()
    equipe = models.BooleanField(default=False)
    surface = models.DecimalField(max_digits=5, decimal_places=2)
    images = models.ImageField(upload_to='annonces/images/', blank=True, null=True)

    def __str__(self):
        return self.titre