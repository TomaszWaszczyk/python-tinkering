class A:
    pass

a1 = A()
a2 = A()

# Do obiektu można dodać atrybut, nawet jeśli nie było o nim mowy w klasie.
a1.imie = 'Ala'
print(a1.imie)

# Ale tem atrybut był dodany tylko do jednego obiektu, nie wpływa na inne obiekty tej klasy
# print(a2.imie)
# a3 = A()
# print(a3.imie)

# To przypomina słowniki.
# To SĄ słowniki !!!

# Atrybuty obiektu są przechowywane w wewnętrznym słowniku, do którego możemy się dostać pisząc __dict__:

slownik = a1.__dict__
print(slownik)

# To nie jest kopia, tylko to jest zawartość tego obiektu.
# Modyfikacje są widoczne w obie strony.
a1.wiek = 30
a1.miasto = 'Warszawa'
print(slownik) # są nowe pola

slownik['imie'] = 'Alicja'
slownik['wiek'] += 1
slownik['nowe'] = 'a kuku'
print(a1.imie, 'ma', a1.wiek, 'lat', a1.nowe) # zmiany widoczne
print()


class B:
    atrybut_klasowy = 'K'

    def __init__(self):
        self.atrybut_obiekotwy = 'O'

    def moja_metoda(self):
        print('jupi')


# Słownik __dict__ obejmuje tylko atrybuty obiektowe (przypisywane bezpośrednio do instancji, zazwyczaj w init)
b1 = B()
b1.drugi_atrybut_obiektowy = 'drugi'
print('obiekt.__dict__', b1.__dict__)

# Atrybuty klasowe są dostępne poprzez klasę. Obejmuje to także metody(!) oraz różne wartości specjalne.
print('Klasa.__dict__', B.__dict__)
print()

# Gdy w Pythonie odwołujemy się do składowej obiektu
# b1.x
# to Python
# 1) poszuka tego w atrybutach obiektowych
# 2) poszuka w atrybutach klasowych
