class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko}, {self.wiek} lat.'


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


def funkcja(a, b, c, x):
    print('Początek funkcji:')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)
    print()

    x += 55
    b.wplata(66)
    a = Konto(a.numer, a.wlasciciel, a.saldo)
    # a.wplata(24)
    a.saldo = 1024
    a.wlasciciel.imie = 'Alicja'
    # Zmiana samej zmiennej, np. x = 100, x += 15, a = Konto(...) - daje efekt lokalny
    # Zmiana wewnątrz obiektu, np. b.wplata(33)  b.saldo += 17  - daje skutek globalny (widzany przez wszystkich)

    print('Koniec funkcji:')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)
    print()


def main():
    ala = Osoba('Ala', 'Kowalska', 20)
    ola = Osoba('Ola', 'Malinowska', 30)
    a = Konto(1, ala, 1000)
    b = Konto(2, ola, 2000)
    c = b
    x = 5000

    print('Początek main:')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)
    print()

    funkcja(a, b, c, x)

    print('Koniec main:')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)
    print()


if __name__ == '__main__':
    main()

