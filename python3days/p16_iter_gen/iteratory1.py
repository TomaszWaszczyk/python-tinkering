# Pętlą for można "iterować" po różnych strukturach danych, np. lista, tupla, napis, zbiór,
# ale też np. plik (jego linie), wyniki zapytania do p17_bazy danych.

lista = [1, 3, 5, 7, 9]
for x in lista:
    print(x)
print()

for litera in 'Ala':
    print(litera)
print()

# Skąd Python wie, po czym można iterować?
# Czy my sami możemy utworzyć taką "rzecz", po której będzie można iterować?

# Odp.: Iterować można po obiektach klas, które są "iterable".
# A to oznacza, że posiadają metodę __iter__, która zwraca "iterator"
# A iterator z kolei ma posiadać metodę __next__, która zwraca kolejny element.

# Można też utworzyć jedną klasę, która posiada __iter__ i __next__ w jednym:
class MojIterator:
    def __init__(self):
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        return self.counter

# Ten iterator jest nieskończony

it = MojIterator()
for x in it:
    print(x)


# To jest równoważne:
# while True:
#     x = it.__next__()
#     print(x)

