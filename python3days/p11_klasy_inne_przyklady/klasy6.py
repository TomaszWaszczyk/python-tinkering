# Przykłady od 2 do 5 to NIE SĄ wzorce do naśladowania.
# Chciałem tylko wytłumaczyć jak działa self / init itp.

# Dopiero to jest "normalna klasa", jakie się tworzy w Pythonie.

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstawSie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def jestPelnoletnia(self):
        return self.wiek >= 18


# Python automatycznie wywołuje metodę __init__ w momencie tworzenia obiektu,
# a wszystkie parametry przekazane w tym miejscu przekazuje do tej metody:
a = Osoba('Ala', 'Kowalska', 30)
b = Osoba('Ola', 'Malinowska', 20)

print(a)
print(b)
print()

a.przedstawSie()
b.przedstawSie()

if a.jestPelnoletnia():
    print(f'{a.imie} może kupić piwo')
else:
    print(f'{a.imie} jest niepełnoletnia')



