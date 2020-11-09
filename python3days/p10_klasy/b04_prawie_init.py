class Osoba:
    def zainicjuj(self, imie, nazwisko, wiek):
        # Przekazane dane zapamiętujęw obiekcie
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        # Zakładając, że obiekt posiada już atrybutry imie, nazwisko, wiek
        # Odczytujemy je z selfa
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def czy_jest_pelnoletnia(self):
        return self.wiek >= 18

a = Osoba()
# Gdy tworzymy obiekt, musimy pamiętać o wywołaniu zainicjuj, żeby ustawiły się wszystkie atrybuty.
a.zainicjuj('Ala', 'Kowalska', 30)
a.przedstaw_sie()

b = Osoba()
b.zainicjuj('Ola', 'Malinowska', 15)
b.przedstaw_sie()

for o in [a, b]:
    if o.czy_jest_pelnoletnia():
        print(o.imie, 'jest pełnoletnia')
    else:
        print(o.imie, 'jest niepełnoletnia')


print()

