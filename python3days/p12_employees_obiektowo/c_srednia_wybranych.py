from employee_v2 import wczytaj_pracownikow

pracownicy = wczytaj_pracownikow('../pracownicy.csv')
suma = 0
ilosc = 0
for p in pracownicy:
    if p.job_title == 'Programmer':
        suma += p.salary
        ilosc += 1

srednia = suma / ilosc
print(srednia)
