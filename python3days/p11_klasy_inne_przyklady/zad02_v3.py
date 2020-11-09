'''
Zaimplementuj klase Employee umozliwiajaca rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej. Jezeli pracownik bedzie pracował wiecej niz 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny policz
jako nadgodziny (z podwójna stawka godzinowa).

Przykład uzycia:
#>>> employee = Employee('Jan', 'Nowak', 100.0)
#>>> employee.register_time(5)
#>>> employee.register_time(5)
#>>> employee.pay_salary()
1000.0
#>>> employee.pay_salary()
0.0
#>>> employee.register_time(10)
#>>> employee.pay_salary()
1200.0
'''

class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.kasa = 0

    def register_time(self, godziny):
        if godziny > 8:
            self.kasa += (godziny - 8) * self.stawka * 2
            self.kasa += 8 * self.stawka
        else:
            self.kasa += godziny * self.stawka

    def pay_salary(self):
        try:
            return self.kasa
        finally:
            self.kasa = 0
            # fragment kodu, który wykona się po wykonaniu treści try,
            # finally wykona się nawet jeśli w try było wywołane return, czy np. był wyrzucony wyjątek


def main():
    employee = Employee('Jan', 'Nowak', 100.0)

    employee.register_time(5)
    employee.register_time(5)
    wynik = employee.pay_salary()
    print(wynik) # 1000

    wynik = employee.pay_salary()
    print(wynik) # 0

    employee.register_time(10)
    wynik = employee.pay_salary()
    print(wynik) # 1200

if __name__ == '__main__':
    main()
