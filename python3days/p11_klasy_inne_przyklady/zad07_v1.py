'''Zaimplementuj klase PremiumEmployee, która bedzie klasa
pochodna Employee. Klasa ta powinna umozliwiac dodatkowo
przyznawanie bonusów pracownikowi.
>>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
>>> employee.register_time(5)
>>> employee.give_bonus(1000.0)
>>> employee.pay_salary()
1500.0
'''

# Wklejam tu jedną z wersji klasy Employee
class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0

    def register_time(self, godziny):
        if godziny > 8:
            self.suma_nadgodzin += godziny - 8
            self.suma_godzin += 8
        else:
            self.suma_godzin += godziny

    def pay_salary(self):
        wynik = self.stawka * self.suma_godzin + 2*self.stawka * self.suma_nadgodzin
        self.suma_godzin = 0
        self.suma_nadgodzin = 0
        return wynik

# I teraz definiuję klasę PremiumEmployee.
class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.suma_bonusow = 0

    def give_bonus(self, bonus):
        self.suma_bonusow += bonus

    def pay_salary(self):
        wynik = super().pay_salary() + self.suma_bonusow
        self.suma_bonusow = 0
        return wynik


def niby_test():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    wynik = employee.pay_salary()
    print(wynik)

if __name__ == '__main__':
    niby_test()
