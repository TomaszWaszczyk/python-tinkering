class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self.numer = numer
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def __str__(self):
        return f'Konto nr {self.numer}, wł.:{self.wlasciciel}, saldo: {self.saldo}'

    def wplata(self, kwota):
        self.saldo += kwota

    def wyplata(self, kwota):
        self.saldo -= kwota


def main():
    # Treść programu umieszczam w funkcji main, głónie po to,
    # aby zmienn konto1, konto2 itp. były zmiennymi lokalnymi, a nie globalnymi.

    konto1 = Konto(1, 'Ala', 1000)
    # print(konto1.__str__())
    # print(str(konto1))
    print(konto1)

    # Zgodnie z zasadami programowania obiektowego nie chcemy bepośrednio modyfikować zmiennych przechowywanych w obiekcie
    # To jest brzydkie:
    # konto1.saldo += 100

    # Chcemy, aby klasa oferowała "metody biznesowe", które dokonują odpowiednich zmian i innych czynności.
    konto1.wplata(100)
    print(konto1)

    konto1.wyplata(400)
    print(konto1)

    konto2 = Konto(2, 'Ola')
    print(konto2)

    konto2.wplata(1500)
    print(konto2)


# Aby main wykonał się gdy uruchamioamy ten plik jako program,
# a nie wykonał się, gdy importujemy.
if __name__ == '__main__':
    main()
