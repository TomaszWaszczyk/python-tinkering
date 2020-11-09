# Podejście do testowania nr 2:
# Testy typu "print"
# Czyli programista wpisuje przykładowe polecenia, wypisuje na ekran ich wyniki,
# i patrzy czy wyniki są właściwe

# Zaleta: łatwiej uruchomić niż program interaktywny
#      bezpośrednio testujemy funkcje
# Wada: trzeba patrzeć co program wypisął, łatwo przeoczyć błąd

from klasa_employee import Employee

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.register_time(5)
wynik = employee.pay_salary()  # 1000
print(wynik)

wynik = employee.pay_salary()  # 0
print(wynik)
print()

employee.register_time(10)
wynik = employee.pay_salary()  # 1200
print(wynik)
print()

# Można utworzyć inny obiekt - każdy liczy swoje godziny i wypłaty osobno
emp2 = Employee('Adam', 'Kowalski', 150.0)
emp2.register_time(3)
wynik = emp2.pay_salary()  # 450
print(wynik)

