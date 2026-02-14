# Importujemy moduł pyplot z biblioteki matplotlib
import matplotlib.pyplot as plt

# Importujemy pandas do wczytania pliku Excel (wymaga openpyxl)
import pandas as pd

# Importujemy numpy do obliczeń pozycji słupków
import numpy as np

# DANE DO WYKRESU

# Wczytujemy dane z pliku Excel 
df = pd.read_excel("oceny11.xlsx")

# Pobieramy listę klas (oś x)
klasy = df["Klasa"]

# Automatycznie pobieramy nazwy przedmiotów
# Są to wszystkie kolumny oprócz kolumny 'Klasa'
przedmioty = df.columns.drop("Klasa")

# TWORZENIE WYKRESU

# Tworzymy nową figurę wykresu
plt.figure(figsize=(10, 6))

# Pozycje bazowe słupków na osi X
x = np.arange(len(klasy))

# Szerokość pojedynczego słupka
szerokosc = 0.8 / len(przedmioty)
# 0.8 to całkowita szerokość grupy słupków dla jednej klasy

# Rysujemy słupki dla każdego przedmiotu w pętli
for i, przedmiot in enumerate(przedmioty):
    plt.bar(
        x + i * szerokosc,
        df[przedmiot],
        width=szerokosc,
        label=przedmiot
    )

# Ustawiamy środek grupy słupków jako pozycję etykiet osi x
plt.xticks(x + szerokosc * (len(przedmioty) - 1) / 2, klasy)

# Tytuł i opisy osi
plt.title("Średnie oceny w klasach", fontsize=14)
plt.xlabel("Klasa")
plt.ylabel("Średnia ocena")

# Siatka 
# linestyle="--" - linia przerywana
# alpha - przezroczystość (0 = niewidoczne, 1 = pełna widoczność)
plt.grid(True, axis="y", linestyle="--", alpha=0.4)

# Legenda
#bbox_to_anchor=(1, 1) - umieszcza legendę poza wykresem w prawym górnym rogu
plt.legend(title="Przedmioty", bbox_to_anchor=(1, 1))

# Automatyczne dopasowanie elementów wykresu
plt.tight_layout()

# Wyświetlenie wykresu
plt.show()
