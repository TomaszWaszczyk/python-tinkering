
class Osoba:
    pass


# Nawet dla pustej klasy można utworzyć obiekty:
a = Osoba()
b = Osoba()

# Technicznie rzecz biorąc, obiekt jest wydzielonym miejscem w pamięci.
print(a, b)

# W obiektach mogą być zapisane "atrybuty". W ten sposób obiekty pamiętają swoje dane.
# W Pythonie - inaczej niż w Javie czy C++ - można dopisywać atrybuty do obiektów
# nawet jeśli nie zostały w żaden sposób zadeklarowane w klasie.
# Nie jest to dobry styl programowania.
a.imie = 'Ala'
a.nazwisko = 'Kowalska'
a.wiek = 30

b.imie = 'Ola'
b.nazwisko = 'Malinowska'
b.wiek = 20

print(a, b)
print()

# Teraz mogę odczytać atrybuty z obiektów
print(a.imie, a.nazwisko, a.wiek)
print(b.imie, b.nazwisko, b.wiek)

a.wiek += 1

print(a.imie, a.nazwisko, a.wiek)
print(b.imie, b.nazwisko, b.wiek)

# Próba odczytania atrybutu, który nie istnieje, kończy się błędem AttributeError.
# print(a.numer_buta)



