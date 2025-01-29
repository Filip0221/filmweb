from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena, Aktor
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera','rok', 'imdb_rating', 'plakat']

class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czasTrwania', 'gatunek']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']

class AktorzyForm(ModelForm):
    class Meta:
        model = Aktor
        fields = ['imie', 'nazwisko']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Adres e-mail')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Nazwa użytkownika",
            "password1": "Hasło",
            "password2": "Potwierdź hasło",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["username"].help_text = "Wymagane. Maksymalnie 150 znaków. Tylko litery, cyfry i @/./+/-/_"
            self.fields[
                "password1"].help_text = "Hasło musi zawierać co najmniej 8 znaków i nie może być całkowicie numeryczne."
            self.fields["password2"].help_text = "Wprowadź to samo hasło ponownie w celu potwierdzenia."