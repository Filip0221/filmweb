# Filmweb Clone

Filmweb Clone to aplikacja internetowa napisana w Django, która pozwala użytkownikom przeglądać bazę filmów, oceniać je i dodawać recenzje. Strona oferuje system logowania oraz personalizację profilu użytkownika.

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

   
## Wygląd
![strona glowna niezalogowany-1](https://github.com/user-attachments/assets/716eb838-0bc3-4535-8fc8-a865ca6b4d01)
![strona głowa zalogowany-1](https://github.com/user-attachments/assets/30499806-e424-458b-93eb-5f08e74bf1de)
![nowy film-1](https://github.com/user-attachments/assets/625a2b7a-d03d-4822-8cc7-0d91c75670e6)
![edycja filmu-1](https://github.com/user-attachments/assets/23fc0e67-1cd1-418f-a080-8945c394809f)
![Szczegóły filmu - Iron man-1](https://github.com/user-attachments/assets/22ee777b-0264-4efe-aa66-810810ec921f)
![logowanie-1](https://github.com/user-attachments/assets/cde8b245-d7f9-47fb-9b3b-fb2f62f96fe5)
![rejstracja-1](https://github.com/user-attachments/assets/dbbd9592-a42d-4913-9750-2be34380036b)
![usuwanie filmu-1](https://github.com/user-attachments/assets/4ddd6dbd-ce3c-4885-93a4-c2d666eed513)

