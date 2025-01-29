from django.urls import path
from .views import wszystkie_filmy, nowy_film, edytuj_film, usun_film, film_szczegoly

urlpatterns = [
    path('wszystkie/', wszystkie_filmy, name="wszystkie_filmy"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
    path('film/<int:id>/', film_szczegoly, name='film_szczegoly')
]
