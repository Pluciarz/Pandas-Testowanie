# Wstępne scenariusze testowe

Dokument zawiera opisy zaplanowanych testów dla biblioteki Pandas.

## Testy funkcjonalne

### 1. Test ładowania danych z pliku CSV
- **Cel:** Sprawdzenie poprawności wczytywania danych z popularnego formatu wymiany danych (CSV).
- **Operacja:** Wczytanie pliku CSV (np. z danymi o użytkownikach: imię, wiek, miasto) za pomocą `pd.read_csv()`.
- **Oczekiwany rezultat:** Obiekt `DataFrame` o odpowiednim kształcie (liczba wierszy, kolumn) i poprawnych typach danych w kolumnach (np. `object` dla imienia, `int` dla wieku).

### 2. Test czyszczenia danych (Not a number)
- **Cel:** Weryfikacja poprawności usuwania wierszy z brakującymi danymi (`NaN`).
- **Operacja:** Na DataFrame zawierającym celowo wprowadzone braki danych (wartości `None`/`NaN`) zastosowanie metody `dropna()`.
- **Oczekiwany rezultat:** Nowy DataFrame, w którym usunięte zostały wszystkie wiersze zawierające jakąkolwiek wartość `NaN`. Sprawdzenie, czy liczba wierszy w nowej ramce jest mniejsza od oryginalnej.

### 3. Test filtrowania danych
- **Cel:** Sprawdzenie, czy mechanizm filtrowania wierszy na podstawie warunku logicznego działa poprawnie.
- **Operacja:** Na DataFrame z danymi (np. o produktach: nazwa, cena, kategoria) zastosowanie filtru, np. `df[df['cena'] > 100]`.
- **Oczekiwany rezultat:** Zwrócenie DataFrame zawierającego tylko te wiersze, dla których warunek jest spełniony. Należy sprawdzić, czy minimalna cena w przefiltrowanym zbiorze jest rzeczywiście większa od 100.

### 4. Test grupowania i agregacji danych
- **Cel:** Weryfikacja poprawności kluczowej funkcjonalności Pandas, jaką jest grupowanie danych (`groupby`) i wyliczanie statystyk agregujących.
- **Operacja:** Na DataFrame z danymi transakcyjnymi (np. `data`, `kategoria`, `sprzedaż`) pogrupowanie dane po kategorii i wyliczenie sumy sprzedaży dla każdej z nich (`groupby('kategoria')['sprzedaż'].sum()`).
- **Oczekiwany rezultat:** Otrzymanie obiektu Series (lub DataFrame) z unikalnymi kategoriami jako indeksem i obliczonymi sumami. Suma wszystkich wartości w kolumnie 'sprzedaż' w oryginalnym DataFrame powinna być równa sumie wszystkich sum po grupach.

### 5. Test łączenia ramek danych (join/merge)
- **Cel:** Sprawdzenie poprawności łączenia dwóch ramek danych na wspólnej kolumnie/indeksie.
- **Operacja:** Połączenie dwóch ramek: jednej z danymi podstawowymi (np. `ID_pracownika`, `imię`) i drugiej z danymi dodatkowymi (`ID_pracownika`, `dział`) za pomocą `pd.merge()`.
- **Oczekiwany rezultat:** Otrzymanie nowej, scalonej ramki danych zawierającej wszystkie kolumny z obu wejściowych ramek. Należy sprawdzić, czy liczba wierszy jest zgodna z oczekiwaniami (np. dla złączenia wewnętrznego - tylko wspólne ID).

## Testy wydajnościowe

### 1. Pomiar czasu operacji sortowania
- **Operacja:** Posortowanie dużego DataFrame (np. 100 000 wierszy) po wybranej kolumnie za pomocą `df.sort_values()`.
- **Pomiar:** Zapisanie czasu wykonania tej operacji do loga. Wynik można później porównać dla różnych wersji Pandas lub różnych rozmiarów danych.

### 2. Pomiar czasu odczytu pliku CSV
- **Operacja:** Odczyt pliku CSV o znacznych rozmiarach (np. 100 MB) za pomocą `pd.read_csv()`.
- **Pomiar:** Zapisanie czasu wykonania operacji odczytu do loga. Jest to istotne z punktu widzenia użytkownika, który często pracuje na dużych zbiorach danych.
