from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor


# admin.site.register(Film)             # tak wyśweitla wszystko

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]   # kontrola co ma się wyświetlać w admin site
    # exclude = ["opis"]                  # wyświetl wszystko poza opisem
    list_display = ["tytul", "imdb_rating", "rok"]  # co ma wyświetlać w liście z wszystkimmi obiektami
    list_filter = ["rok"]  # okno filtrowania z boku listy
    search_fields = ("tytul", "opis")  # okno wyszukiwania nad listą


admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)