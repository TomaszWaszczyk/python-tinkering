# Podejście do testowania nr 3:
# Niech program testujący sam sprawdzi czy wyszły dobre wyniki.

# To już koncepcyjnie rzecz biorąc są p19_testy jednostkowe.


from klasa_employee import Employee

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.register_time(5)

wynik = employee.pay_salary()
if wynik == 1000:
    print('test 1: OK')
else:
    print('test 1: FAIL')


wynik = employee.pay_salary()
if wynik == 0:
    print('test 2: OK')
else:
    print('test 2: FAIL')

employee.register_time(10)
wynik = employee.pay_salary()
if wynik == 1200:
    print('test 3: OK')
else:
    print('test 3: FAIL')

emp2 = Employee('Adam', 'Kowalski', 150.0)
emp2.register_time(3)
wynik = emp2.pay_salary()
if wynik == 450:
    print('test 4: OK')
else:
    print('test 4: FAIL')
