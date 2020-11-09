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


# Jeśli klasa Employee jest nbapisana w taki sposób, że zampamiętuje pieniądze w zmiennej kasa,
# to implementacja PRemiumEmployee może być dużo prostsza - można doliczać bonusy bezpośrednio do zmiennej kasa.

# Takie podejście do programowania, że korzystamy ze szczegółów sposobu implementacji klasy A
# podczas definiowania klasy B jest jednak łamaniem zasady "enkapsulacji" i w poważniejszych projektach powinniśmy tego unikać.
# Problem:  jeśli teraz ktoś zmieni szczegóły klasy Employee, to PremiumEmployee może przestać działać.
class PremiumEmployee(Employee):
    def give_bonus(self, bonus):
        self.kasa += bonus


employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
wynik = employee.pay_salary()
print(wynik)

