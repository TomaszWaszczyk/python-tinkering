import copy

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f'{self.imie} {self.nazwisko}, {self.wiek} lat'


class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def __str__(self):
        return f'Konto nr {self.numer}, saldo: {self.saldo}, wł.: {self.wlasciciel}'

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
    b.wplata(40)

    a.wplata(10)

    # głęboka kopia tworzy nowy obiekt i kopiuje również obiekty, na które konto wskazywało (itd. itd. itd...)
    a = copy.deepcopy(a)
    a.wplata(7)
    a.wlasciciel.imie = 'Alicja'

    print('Koniec funkcji:')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)
    print()


def main():
    ala = Osoba('Ala', 'Kowalska', 30)
    ola = Osoba('Ola', 'Malinowska', 40)

    a = Konto(1, ala, 1000)
    b = Konto(2, ola, 2000)
    c = b
    x = 5000

    print('Początek main')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)
    print()

    funkcja(a, b, c, x)

    print('Po powrocie z funkcji, znowu w main:')
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('x:', x)


if __name__ == '__main__':
    main()

