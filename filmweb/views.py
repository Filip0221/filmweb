from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film, DodatkoweInfo, Ocena, Aktor
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm, AktorzyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})


@login_required
def nowy_film(request):
    if not request.user.is_superuser:
        return HttpResponse("Tylko administratorzy mogą dodawać filmy.", status=403)
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)
    return render(request, 'film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'nowy': True})


@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if not request.user.is_superuser:
        return HttpResponse("Tylko administratorzy mogą edytować filmy.", status=403)
    oceny = Ocena.objects.filter(film=film)
    aktorzy = film.aktorzy.all()

    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            if form_ocena.is_valid():
                ocena = form_ocena.save(commit=False)
                ocena.film = film
                ocena.user = request.user
                ocena.save()

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)
    return render(request, 'film_form.html',
                  {'form': form_film, 'form_dodatkowe': form_dodatkowe, "oceny": oceny, 'form_ocena': form_ocena,
                   'aktorzy': aktorzy, 'nowy': False})


@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if not request.user.is_superuser:
        return HttpResponse("Tylko administratorzy mogą usuwać filmy.", status=403)
    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film, })

def film_szczegoly(request, id):
    film = get_object_or_404(Film, id=id)
    oceny = film.ocena_set.all()
    aktorzy = film.aktorzy.all()
    form_ocena = OcenaForm(request.POST or None)

    if request.method == 'POST':
        if form_ocena.is_valid():
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.user = request.user
            ocena.save()
            return redirect('film_szczegoly', id=film.id)

    return render(request, 'film_szczegoly.html', {'film': film, 'oceny': oceny, 'aktorzy': aktorzy, 'form_ocena': form_ocena,})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Twoje konto zostało utworzone. Możesz się teraz zalogować.")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form})