# Importujemy moduł pyplot z biblioteki matplotlib 
import matplotlib.pyplot as plt

# DANE DO WYKRESU

# Lista z nazwami miesięcy
# Te wartości będą użyte jako etykiety osi x 
miesiace = ["Kwiecień", "Maj", "Czerwiec", "Lipiec"]

# Listy z temperaturami dla poszczególnych miast
# Każda liczba odpowiada miesiącowi o tym samym indeksie w liście 'miesiace':
warszawa = [13, 19, 22, 24]
krakow   = [12, 18, 21, 23]
gdansk   = [9, 15, 19, 21]

# TWORZENIE WYKRESU

# Tworzymy nową "figurę" wykresu o konkretnym rozmiarze
# figsize=(szerokość, wysokość)
plt.figure(figsize=(10, 6))

# Linia dla Warszawy
# plt.plot(x, y, ...) tworzy wykres liniowy:
# x - miesiace 
# y - warszawa
# color="red" - kolor linii
# marker="o" - kształt punktów jako kółka
# linewidth=2.5 - grubość linii
# markersize=8 - rozmiar markerów
# label="Warsza" - tekst, który pojawi się w legendzie
plt.plot(miesiace, warszawa, color= "red", marker="o", linewidth=2.5, markersize=8, label="Warszawa")

# Rysujemy analogicznie linię dla Krakowa.
# marker="D" - diamond
plt.plot(miesiace, krakow, color= "green", marker="D", linewidth=2.5, markersize=8, label="Kraków")

# Rysujemy analogicznie linię dla Gdańska.
# marker="s" - square
plt.plot(miesiace, gdansk, color= "blue", marker="s", linewidth=2.5, markersize=8, label="Gdańsk")

# Ustawiamy tytuł wykresu.
# fontsize=18 - rozmiar czcionki tytułu
# fontweight="bold" - pogrubienie tytułu
plt.title("Średnia temperatura w polskich miastach (2024)", fontsize=18, fontweight="bold")

# Opis osi x
# fontsize=13 - rozmiar czcionki opisu osi
plt.xlabel("Miesiąc", fontsize=13)

# Analogicznie opis osi y
plt.ylabel("Temperatura (°C)", fontsize=13)

# grid siatka na wykresie - True włącza, False wyłącza
# linestyle="--" - linia przerywana
# alpha=0.5 - przezroczystość (0 = niewidoczne, 1 = pełna widoczność)
plt.grid(True, linestyle="--", alpha=0.5)

# Opis linii - legenda
# legend() zbiera etykiety z parametru label
# title="Miasto" - tytuł legendy
# loc="upper left" - położenie legendy (lewy górny róg)
plt.legend(title="Miasto", loc="upper left")

# Automatycznie dopasowanie elementów na wykresie 
plt.tight_layout()

# Wyświetlanie wykresu 
plt.show()
