# Importujemy moduł pyplot z biblioteki matplotlib
import matplotlib.pyplot as plt

# DANE DO WYKRESU

# Lista z godzinami
# Te wartości będą użyte jako etykiety osi x
godziny = ["8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]

# Lista z liczbą odwiedzin strony w poszczególnych godzinach
# Każda liczba odpowiada godzinie o tym samym indeksie w liście 'godziny'
odwiedziny = [450, 700, 1200, 900, 1100, 1400, 1700, 900]

# TWORZENIE WYKRESU

# Tworzymy nową "figurę" wykresu o konkretnym rozmiarze
# figsize=(szerokość, wysokość)
plt.figure(figsize=(10, 6))

# Rysujemy wykres liniowy przedstawiający ruch na stronie
# plt.plot(x, y, ...) tworzy wykres liniowy:
# x - godziny
# y - odwiedziny
# color="red" - kolor linii
# marker="^" - kształt punktów trójkąt
# linewidth=2.5 - grubość linii
# markersize=8 - rozmiar markerów
plt.plot(godziny, odwiedziny, color="red", marker="^", linewidth=2.5, markersize=8)

# Wypełnienie obszaru pod wykresem kolorem
# alpha=0.2 - przezroczystość wypełnienia
plt.fill_between(godziny, odwiedziny, color="red", alpha=0.2)

# Średnią liczbę odwiedzin
srednia = sum(odwiedziny) / len(odwiedziny)

# Rysujemy poziomą linię oznaczającą średnią liczbę odwiedzin
# linestyle=":" - linia kropkowana
# color="blue" - kolor linii
# linewidth=2 - grubość linii
# label - opis linii w legendzie
plt.axhline(y=srednia, color="blue", linestyle=":", linewidth=2, label=f"Średnia liczba odwiedzin ({int(srednia)})")

# Tytuł wykresu
# fontsize=16 - rozmiar czcionki
plt.title("Ruch na stronie internetowej - 24 sierpnia 2025", fontsize=16)

# plt.text(x, y, tekst) - dodaje tekst w wybranym miejscu wykresu
# x=0 - początek osi x (pierwsza pozycja)
# y=srednia + 30 - lekko nad linią, żeby tekst nie wchodził w linię
plt.text(0, srednia + 30, f"Średnia liczba odwiedzin ({int(srednia)})", color="blue")

# Opis osi x
plt.xlabel("Godzina")

# Opis osi y
plt.ylabel("Liczba odwiedzin")

# Siatka 
# linestyle="--" - linia przerywana
# alpha - przezroczystość (0 = niewidoczne, 1 = pełna widoczność)
plt.grid(True, linestyle="--", alpha=0.4)

# Automatycznie dopasowanie elementów na wykresie
plt.tight_layout()

# Wyświetlanie wykresu
plt.show()
