
class Osoba:
    # W klasie można definiować "metody":
    def przedstawSie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')


# Nawet dla pustej klasy można utworzyć obiekty:
a = Osoba()
b = Osoba()
print(a, b)

# Ustawiam atrybuty obiektów
a.imie = 'Ala'
a.nazwisko = 'Kowalska'
a.wiek = 30

b.imie = 'Ola'
b.nazwisko = 'Malinowska'
b.wiek = 20

# Python wywoła metodę przedstawSie z klasy Osoba, obiekt "a" przekaże jako parametr self
a.przedstawSie()

# A teraz jako self przekazywany jest obiekt "b"
b.przedstawSie()
print()

c = Osoba()
c.imie = 'Celina'
c.nazwisko = 'Celinowska'
# Powiedzmy, że zapomniałem ustawić atrybut wiek...
# c.przedstawSie()
# AttributeError: 'Osoba' object has no attribute 'wiek'

# Morał: wszystkie atrybuty obiektu, które są mu potrzebne do pracy (do działania jego metod),
# powinny być ustawione w momencie tworzenia obiektu.
# Rozwiązanie: metoda __init__

