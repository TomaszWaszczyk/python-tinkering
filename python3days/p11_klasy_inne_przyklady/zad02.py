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
        self.suma_godzin = 0

    def register_time(self, godziny):
        if godziny > 8:
            nadgodziny = godziny - 8
        else:
            nadgodziny = 0
        self.suma_godzin += godziny + nadgodziny

    def pay_salary(self):
        wynik = self.stawka * self.suma_godzin
        self.suma_godzin = 0
        return wynik


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
