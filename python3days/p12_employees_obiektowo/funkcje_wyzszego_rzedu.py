import employee_v2

lista = employee_v2.wczytaj_pracownikow('pracownicy.csv')

# Średnia pensja wszystkich za pomocą wyliczeń listowych:
pensje = [emp.salary for emp in lista]
srednia = sum(pensje) / len(pensje)
print(srednia)

# Średnia pensja wszystkich za pomocą map:
pensje = list(map(lambda emp: emp.salary, lista))
srednia = sum(pensje) / len(pensje)
print(srednia)

# Średnia pensja programistów za pomocą wyliczeń listowych:
pensje = [emp.salary for emp in lista if emp.job_title == 'Programmer']
srednia = sum(pensje) / len(pensje)
print(srednia)

# Średnia pensja programistów za map i filter:
pensje = list(map(lambda emp: emp.salary, filter(lambda emp: emp.job_title == 'Programmer', lista)))
srednia = sum(pensje) / len(pensje)
print(srednia)

wynik_filtrowania = filter(lambda emp: emp.job_title == 'Programmer', lista)
wynik_mapowania = map(lambda emp: emp.salary, wynik_filtrowania)
pensje = list(wynik_mapowania)
srednia = sum(pensje) / len(pensje)
print(srednia)

# lambda to jest tylko inny sposób definiowana funkcji. można zrobić też tak:
def get_salary(emp):
    return emp.salary

pensje = list(map(get_salary, lista))
srednia = sum(pensje) / len(pensje)
print(srednia)
