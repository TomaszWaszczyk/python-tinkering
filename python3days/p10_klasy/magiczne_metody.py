
class OpakowanaLiczba:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    # Tekstowa reprezentacja obiektu - dla człowieka.
    def __str__(self):
        return f'[{self.wartosc}]'

    # Tekstowa reprezentacja obiektu - techniczna; najlepiej, aby z takiego tekstu Python był w stanie utworzyć obiekt.
    def __repr__(self):
        return f'OpakowanaLiczba({repr(self.wartosc)})'

    # Definiując metody takie jak __add__, __sub__, __mul__
    # Możemy określić jak będą działać operatory + - * itd. dla obiektów tej klasy
    def __add__(self, other):
        wynik = self.wartosc + other.wartosc
        return OpakowanaLiczba(wynik)

    def __mul__(self, other):
        wynik = self.wartosc * other.wartosc
        return OpakowanaLiczba(wynik)

    # __eq__, __lt__, __ge__ itd. - określają działanie operatorów porównania
    # wynikiem ma być True albo False
    def __eq__(self, other):
        return self.wartosc == other.wartosc

    def __lt__(self, other):
        return self.wartosc < other.wartosc


# Właśnie w taki sposób twórcy różnych standardowych klas Pythona byli w stanie zdefiniować dizałanie tych operatów

x = OpakowanaLiczba(5)
y = OpakowanaLiczba(7)

print('x:', x)
print('y:', y)

print(repr(x))
print(repr(y))
print()

suma = x + y
print('suma:', suma)

iloczyn = x * y
print('iloczyn:', iloczyn)

if x < y:
    print('mniejsze')
else:
    print('większe lub równe')




