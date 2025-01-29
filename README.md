# Filmweb Clone

Filmweb Clone to aplikacja internetowa napisana w Django, która pozwala użytkownikom przeglądać bazę filmów, oceniać je i dodawać recenzje. Strona oferuje system logowania oraz personalizację profilu użytkownika.

## Wygląd
![strona glowna niezalogowany-1](https://github.com/user-attachments/assets/716eb838-0bc3-4535-8fc8-a865ca6b4d01)

## Funkcje

- **Autoryzacja użytkowników** – rejestracja, logowanie, resetowanie hasła.
- **Przeglądanie filmów** – lista filmów z wyszukiwarką i filtrami.
- **System ocen i recenzji** – użytkownicy mogą dodawać oceny i komentarze do filmów.
- **Profile użytkowników** – każdy użytkownik może zobaczyć swoje recenzje i ocenione filmy.
- **Panel administracyjny** – zarządzanie filmami i użytkownikami.

## Technologie

- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Baza danych: SQLite / PostgreSQL
- Autoryzacja: Django Authentication

## Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-repo.git
   cd filmweb-clone
   ```
2. Utwórz i aktywuj wirtualne środowisko:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```
4. Wykonaj migracje:
   ```bash
   python manage.py migrate
   ```
5. Uruchom serwer:
   ```bash
   python manage.py runserver
   ```
