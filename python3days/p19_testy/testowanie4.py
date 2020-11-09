
from klasa_employee import Employee

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.register_time(5)

wynik = employee.pay_salary()
assert wynik == 1000

wynik = employee.pay_salary()
assert wynik == 0

employee.register_time(10)
wynik = employee.pay_salary()
assert wynik == 1200

emp2 = Employee('Adam', 'Kowalski', 150.0)
emp2.register_time(3)
wynik = emp2.pay_salary()
assert wynik == 450
