# Cel: dla każdego stanowiska (bez powtórzeń)
# wypisz ilu jest pracowników na tym stanowisku i jaka jest ich średnia pensja

from employee_v2 import *

pracownicy = wczytaj_pracownikow('../pracownicy.csv')

jobs = set()
for p in pracownicy:
    jobs.add(p.job_title)

print(f'Wszystkie joby ({len(jobs)}):')

for job in jobs:
    suma = 0
    ilosc = 0
    for p in pracownicy:
        if p.job_title == job:
            suma += p.salary
            ilosc += 1
    srednia = suma / ilosc
    print(f'{job:32} {ilosc:2} {srednia:10.2f}')
