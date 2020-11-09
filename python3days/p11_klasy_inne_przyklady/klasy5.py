
class Osoba:
    # amatorska namiastka metody __init__ - żeby zrozumieć jak to działa
    def zainicjuj(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstawSie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')


a = Osoba()
# po utworzeniu obiektu od razu ustawiam wszystkie atrybuty za pomocą metody
a.zainicjuj('Ala', 'Kowalska', 30)

b = Osoba()
b.zainicjuj('Ola', 'Malinowska', 20)

a.przedstawSie()
b.przedstawSie()


