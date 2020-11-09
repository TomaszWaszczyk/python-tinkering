class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        # Ta metoda powinna w wyniku zwracać napis - Python użyje tego napisu,
        # gdy będzie wypisywał ten obiekt w postaci tekstowej.
        return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

    def przedstawSie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def jestPelnoletnia(self):
        return self.wiek >= 18


a = Osoba('Ala', 'Kowalska', 30)
b = Osoba('Ola', 'Malinowska', 20)

print(a)
print(b)
print()

a.przedstawSie()
b.przedstawSie()
print()

if a.jestPelnoletnia():
    print(f'{a.imie} może kupić piwo')
else:
    print(f'{a.imie} jest niepełnoletnia')
