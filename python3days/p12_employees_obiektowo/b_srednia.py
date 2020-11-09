from employee_v2 import wczytaj_pracownikow

pracownicy = wczytaj_pracownikow('../pracownicy.csv')
suma = 0
for p in pracownicy:
    suma += p.salary

srednia = suma / len(pracownicy)
print(srednia)
