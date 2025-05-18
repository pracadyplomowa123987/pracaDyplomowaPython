# 🧪 Formularz kontaktowy – Testy automatyczne (Selenium + PyTest)
Projekt przedstawia zestaw testów automatycznych dla formularza kontaktowego dostępnego na stronie [https://candymapper.com](https://candymapper.com). Testy zostały napisane w Pythonie z użyciem Selenium WebDriver, przy wykorzystaniu wzorca Page Object Model (POM).

## 🛠️ Technologie

- Python: 3.13.3
- pytest: 8.3.5
- pytest-html: 4.1.1 
- selenium: 4.32.0
- faker: 37.3.0
- Przeglądarka: Chrome
- WebDriver: ChromeDriver 

## 🚀 Instalacje
- pip install selenium
- pip install pytest
- pip install pytest-html
- pip install Faker

## 🧪 Zakres testów
1. Test - walidacja formularza kontaktowego przy próbie wysłania pustego formularza.
2. Test - walidacja formularza kontaktowego przy próbie wysłania formularza bez obowiązkowego pola Email.
3. Test - walidacja formularza kontaktowego przy próbie wysłania formularza z niepoprawnym Email.
4. Test - weryfikacja poprawnie uzupełnionego formularza
5. Test - Thank you page weryfikacja tekstu

## 🔧 Konfiguracja i automatyzacja

- W pliku conftest.py znajduje się konfiguracja drivera oraz setup folderów na raporty.
- Zastosowano faker do generowania imienia, nazwiska, maila, numeru telefonu i wiadomości.
- Kroki testowe rejestrowane są za pomocą print() i widoczne w raporcie (sekcja Captured stdout call).
- Kod został oparty na uniwersalnych metodach, co umożliwia np. wskazywanie elementów do scrollowania dynamicznie.

## 📌 Cel projektu
Testy przygotowane jako projekt dyplomowy w ramach studiów podyplomowych z testowania oprogramowania.
