from employee_v2 import wczytaj_pracownikow

job = input('Podaj nazwę stanowiska: ')

pracownicy = wczytaj_pracownikow('../pracownicy.csv')
suma = 0
ilosc = 0
for p in pracownicy:
    if p.job_title.lower() == job.lower():
        suma += p.salary
        ilosc += 1

srednia = suma / ilosc
print(srednia)
