from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class DodatkoweInfo(models.Model):

    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horro'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Drama'),
    }
    czasTrwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return self.tytul + ' (' + str(self.rok) + ')'

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if not (1 <= self.gwiazdki <= 10):
            raise ValidationError({'gwiazdki': 'Ocena musi być liczbą od 1 do 10.'})

class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film, related_name='aktorzy')