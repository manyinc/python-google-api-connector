# Google Api Spreadsheet Connector

Google Api Spreadsheet Connector to aplikacja w języku Python, która pobiera dane z Google Sheets za pomocą OAuth2 i biblioteki `gspread`. Poniższy przewodnik poprowadzi Cię przez proces instalacji i konfiguracji tego programu.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz zainstalowane poniższe narzędzia:
- Python 3.6 lub nowszy
- Konto Google z dostępem do Google Sheets
- Klucz usługi (service account key) w formacie JSON z uprawnieniami do odczytu/zapisu do wybranego arkusza Google Sheets

## Instalacja

1. **Klonowanie repozytorium**

    ```bash
    git clone https://github.com/manyinc/python-google-api-connector.git
    cd python-google-api-connector
    ```

2. **Tworzenie i aktywacja wirtualnego środowiska**

    Zaleca się użycie wirtualnego środowiska w celu izolacji zależności:

    ```bash
    python -m venv venv
    source venv/bin/activate   # Dla systemów Unix/MacOS
    .\venv\Scripts\activate    # Dla systemu Windows
    ```

3. **Instalacja zależności**

    Użyj `pip`, aby zainstalować wymagane pakiety:

    ```bash
    pip install -r requirements.txt
    ```

4. **Konfiguracja autoryzacji**

    Skopiuj swój plik klucza usługi JSON do katalogu `auth/` i nazwij go `creds.json`. Powinno to wyglądać tak:

    ```plaintext
    python-google-api-connector/
    ├── auth/
    │   └── creds.json
    ├── main.py
    └── requirements.txt
    ```

5. **Konfiguracja Google API**

   - Utwórz arkusz google 'usersdb'
   - Przejdź do strony https://console.cloud.google.com/
   - Postępuj zgodnie ze screenami z pliku `google-api-cfg.pdf`.

## Użycie

1. **Uruchomienie skryptu**

    Po wykonaniu powyższych kroków możesz uruchomić skrypt:

    ```bash
    python main.py
    ```

2. **Wyświetlanie wyników**

    Skrypt pobierze dane z pierwszego arkusza (`worksheet`) w pliku Google Sheets o nazwie `usersdb` i wydrukuje je w konsoli.
