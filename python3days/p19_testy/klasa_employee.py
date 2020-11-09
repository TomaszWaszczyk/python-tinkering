
class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.kasa = 0

    def register_time(self, godziny):
        if godziny <= 8:
            self.kasa += godziny * self.stawka
        else:
            self.kasa += 8 * self.stawka
            self.kasa += (godziny - 8) * 2 * self.stawka

    def pay_salary(self):
        try:
            return self.kasa
        finally:
            self.kasa = 0
