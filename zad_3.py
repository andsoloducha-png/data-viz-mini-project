# Importujemy moduł pyplot z biblioteki matplotlib
import matplotlib.pyplot as plt

# Importujemy pandas do wczytania pliku Excel (wymaga openpyxl)
import pandas as pd

# DANE DO WYKRESU

# Wczytujemy dane z pliku Excel
df = pd.read_excel("ceny22.xlsx")

# Tworzymy wykres liniowy o wymiarach
plt.figure(figsize=(12, 7))

# Pobieramy unikalne nazwy produktów
produkty = df["Rodzaje produktów"].unique()

# Rysujemy linię dla każdego produktu
for produkt in produkty:
    # Filtrujemy dane dla konkretnego produktu
    dane_produktu = df[df["Rodzaje produktów"] == produkt]
    
    # Rysujemy linię z markerami
    plt.plot(dane_produktu["Rok"], dane_produktu["Wartosc"], marker='o', markersize=8, linewidth=2.5, label=produkt)

# Dynamicznie pobierny zakres lat z danych
rok_min = df["Rok"].min()
rok_max = df["Rok"].max()

# Ustawiamy tytuł wykresu z dynamicznymi latami
plt.title(f"Zmiany cen wybranych produktów rybnych w latach {rok_min}-{rok_max}", fontsize=16, fontweight='bold')

# Opisy osi
plt.xlabel("Rok", fontsize=13, fontweight='bold')
plt.ylabel("Cena (zł/kg)", fontsize=13, fontweight='bold')

# Siatka pomocnicza dla lepszej czytelności
plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)

# Legenda z nazwami produktów
plt.legend(title="Produkty", bbox_to_anchor=(1, 1))

# Dynamiczny zakres osi X - automatycznie dopasuje się do danych
plt.xlim(rok_min - 0.5, rok_max + 0.5)

# Formatujemy oś Y - od 0 do maksymalnej wartości + margines
plt.ylim(0, df["Wartosc"].max() * 1.15)

# Automatyczne dopasowanie elementów wykresu
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()