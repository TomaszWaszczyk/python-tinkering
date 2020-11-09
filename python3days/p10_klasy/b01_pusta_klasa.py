class Osoba:
    pass


a = Osoba()
print(a)

# W Pythonie obiekt to jest po prostu pudełko, w którym można umieszczać różne wartości.
# Działa jak pewien rodzaj słownika.

a.imie = 'Ala'
a.wiek = 20
print(a.imie, 'ma', a.wiek, 'lat')

# Tylko ten obiekt, w którym zapisałem atrybut, posiada taki atrybut. Inne obiekty tej samej klasy nie...
b = Osoba()
#ERR print(b.imie)
