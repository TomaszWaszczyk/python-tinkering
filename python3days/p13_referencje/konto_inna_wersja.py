# W Pythonie nie ma zmiennych i metod prywatnych - język nie ma takich mechanizmów.
# Ale atrybuty, których nazwy rozpoczynają się od _  są traktowane: "programista chciałby, żeby były prywatne".

class Konto:
    def __init__(self, numer, wlasciciel, saldo=0):
        self._numer = numer
        self._wlasciciel = wlasciciel
        self._saldo = saldo
        # istnieje możliwość, aby utworzyć atrybut nie przekazany jako parametr inita
        self._historia = []
        self._historia.append(f'stan początkowy: {saldo}')

    def __str__(self):
        return f'Konto nr {self._numer}, wł. {self._wlasciciel}, saldo: {self._saldo} PLN'

    def wplata(self, kwota):
        self._saldo += kwota
        self._historia.append(f'wpłata {kwota}')

    def wyplata(self, kwota):
        self._saldo -= kwota
        self._historia.append(f'wypłata {kwota}')

    def wypisz_historie(self):
        print(f'Historia rachunku nr {self._numer}')
        for h in self._historia:
            print(h)
        print(f'Stan końcowy: {self._saldo}')
        print()


k1 = Konto(1, 'Ala', 5000)
print(k1)

k2 = Konto(2, 'Ola')
print(k2)

print()

k1.wplata(300)
print(k1)  # 5300, saldo ma ulec zmianie

k1.wyplata(1000)
print(k1)  # 4300
print()

k2.wplata(3333)
print(k2)
print()

k1.wypisz_historie()

# Python nie zabroni odczytu zmiennej "prywatnej" - bo sam interpreter/język tego nie pilnuje.
# Ale np. Pycharm nie podpowiada takich zmiennych podczas piania kodu.
print(k1._saldo)

