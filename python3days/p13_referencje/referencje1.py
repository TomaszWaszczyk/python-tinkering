class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def __str__(self):
        return f'Konto nr {self.numer}, wł. {self.wlasciciel}, saldo: {self.saldo} PLN'

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        self.saldo -= kwota


a = Konto(1, 'Ala', 1000)
b = Konto(2, 'Ola', 2000)
c = b

print('a:', a)
print('b:', b)
print('c:', c)
print()

a.wplata(1)
print('a:', a)
print('b:', b)
print('c:', c)
print()

b.wplata(40)
print('a:', a)
print('b:', b)
print('c:', c)
print()

c.wplata(8)
print('a:', a)
print('b:', b)
print('c:', c)
print()

b = a
print('a:', a)
print('b:', b)
print('c:', c)
print()

c = a
# teraz wszystkie 3 zmienne wskazują na pierwsze konto, a o drugim "zapominamy"
print('a:', a)
print('b:', b)
print('c:', c)
print()

# jeśli chcemy jawnie wpisać, że zmienna nie wskazuje na żaden obiekt, to można tak:
a = None
print('a:', a)
print('b:', b)
print('c:', c)
print()

# w Pythonie można jawnie usunąć zmienną globalną,
# ale to nie oznacza usunięcia obiektu (inaczej niż delete w C++)
del b

# od tej pory nie mogę używać tej nazwy zmiennej,
# ale jeśli istnieje inna zmienna wskazująca na obiekt, to obiekt wciąż żyje i można go używać
print('a:', a)
# print('b:', b) # NameError: name 'b' is not defined
print('c:', c)
