from zad02 import Employee

# te p19_testy można uruchomić za pomocą pytest

def test_employee_normalne_godziny():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.register_time(5)
    wynik = employee.pay_salary()
    assert wynik == 1000

# różne scenariusze zapisujemy w osobnych funkcjach
def test_employee_nadgodziny():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    wynik = employee.pay_salary()
    assert wynik == 1200

def test_employee_zerowanie():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    employee.register_time(10)
    employee.pay_salary()
    # w tym teście nie interesuje mnie wynik pierwszego pay_salary, tylko drugiego
    wynik = employee.pay_salary()
    assert wynik == 0

def test_employee_inna_stawka():
    emp2 = Employee('Adam', 'Kowalski', 150.0)
    emp2.register_time(3)
    wynik = emp2.pay_salary()
    assert wynik == 450