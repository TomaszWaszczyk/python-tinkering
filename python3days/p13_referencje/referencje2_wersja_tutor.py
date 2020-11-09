# http://www.pythontutor.com/visualize.html

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
    x += 55
    b.wplata(40)
    a.wplata(10)

    a = Konto(a.numer, a.wlasciciel, a.saldo)
    a.wplata(7)
    a.wlasciciel.imie = 'Alicja'
    pass


def main():
    ala = Osoba('Ala', 'Kowalska', 30)
    ola = Osoba('Ola', 'Malinowska', 40)

    a = Konto(1, ala, 1000)
    b = Konto(2, ola, 2000)
    c = b
    x = 5000

    funkcja(a, b, c, x)

    pass


if __name__ == '__main__':
    main()

