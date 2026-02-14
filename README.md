# Wizualizacja Danych i Techniki Data Mining

Projekt zawiera skrypty do wizualizacji danych przy użyciu biblioteki Matplotlib i Pandas.

## Struktura projektu

```
.
├── README.md
├── requirements.txt
├── zad_1_wykres_1.py      # Wykres liniowy - temperatury w miastach
├── zad_1_wykres_2.py      # Wykres liniowy - ruch na stronie
├── zad_2.py               # Wykres słupkowy - średnie ocen
├── zad_3.py               # Wykres liniowy - zmiany cen
├── oceny11.xlsx           # Dane do zadania 2
└── ceny22.xlsx            # Dane do zadania 3
```

## Opis zadań

### Zadanie 1 - Wykresy liniowe z danymi statycznymi

#### `zad_1_wykres_1.py` - Temperatura w miastach
- **Typ wykresu**: Wykres liniowy
- **Dane**: Średnie temperatury w Warszawie, Krakowie i Gdańsku (kwiecień-lipiec 2024)
- **Funkcje**: Wiele serii danych, różne markery, legenda, siatka

#### `zad_1_wykres_2.py` - Ruch na stronie internetowej
- **Typ wykresu**: Wykres liniowy z wypełnieniem
- **Dane**: Liczba odwiedzin strony w ciągu dnia (24 sierpnia 2025)
- **Funkcje**: Wypełnienie obszaru pod wykresem, linia średniej, etykiety tekstowe

### Zadanie 2 - Wykres słupkowy z pliku Excel

#### `zad_2.py` - Średnie ocen w klasach
- **Typ wykresu**: Wykres słupkowy grupowany
- **Źródło danych**: `oceny11.xlsx`
- **Funkcje**: 
  - Automatyczne wczytywanie klas i przedmiotów z pliku Excel
  - Dynamiczne dostosowanie do nowych przedmiotów i klas
  - Grupowanie słupków według klas

**Format danych w `oceny11.xlsx`:**
| Klasa    | Matematyka | Polski | Angielski |
|----------|------------|--------|-----------|
| Klasa 1A | 4.2        | 4.5    | 4.8       |

### Zadanie 3 - Wykres liniowy z pliku Excel

#### `zad_3.py` - Zmiany cen produktów rybnych
- **Typ wykresu**: Wykres liniowy wieloseriowy
- **Źródło danych**: `ceny22.xlsx`
- **Funkcje**:
  - Automatyczne wykrywanie produktów i lat z pliku Excel
  - Dynamiczne dostosowanie do nowych produktów i zakresów dat
  - Osobna linia dla każdego produktu

**Format danych w `ceny22.xlsx`:**
| Rodzaje produktów | Rok  | Wartosc |
|-------------------|------|---------|
| pstrąg świeży...  | 2010 | 11.23   |

## Instalacja

### Wymagania
- Python 3.7 lub nowszy
- pip (menedżer pakietów Python)

### Krok 1: Klonowanie repozytorium
```bash
git clone <url-repozytorium>
cd <nazwa-katalogu>
```

### Krok 2: Utworzenie wirtualnego środowiska (opcjonalne, ale zalecane)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Krok 3: Instalacja bibliotek
```bash
pip install -r requirements.txt
```

lub ręcznie:
```bash
pip install matplotlib pandas openpyxl numpy
```

##  Uruchamianie

Każdy skrypt można uruchomić niezależnie:

```bash
python zad_1_wykres_1.py
python zad_1_wykres_2.py
python zad_2.py
python zad_3.py
```

**Uwaga:** Pliki `oceny11.xlsx` i `ceny22.xlsx` muszą znajdować się w tym samym katalogu co skrypty `zad_2.py` i `zad_3.py`.

## Zależności

- **matplotlib** - biblioteka do tworzenia wykresów
- **pandas** - biblioteka do analizy danych
- **openpyxl** - obsługa plików Excel (.xlsx)
- **numpy** - obliczenia numeryczne

## Rozszerzanie projektu

### Zadanie 2 - Dodawanie nowych przedmiotów/klas
Wystarczy dodać kolumny lub wiersze w pliku `oceny11.xlsx`. Skrypt automatycznie wykryje zmiany.

### Zadanie 3 - Dodawanie nowych produktów/lat
Dodaj nowe wiersze w pliku `ceny22.xlsx` z produktami lub latami. Wykres automatycznie się dostosuje.

## Notatki techniczne

- Wszystkie wykresy używają polskich opisów i etykiet
- Wykresy są responsywne i automatycznie dopasowują rozmiar
- Użyto `plt.tight_layout()` do optymalnego rozmieszczenia elementów
- Siatka ułatwia odczyt wartości z wykresów

## Autor

Projekt edukacyjny z przedmiotu "Wizualizacja Danych i Techniki Data Mining"

## Licencja

Projekt edukacyjny - wolny do użytku
