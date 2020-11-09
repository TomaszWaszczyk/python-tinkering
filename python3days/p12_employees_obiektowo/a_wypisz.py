from employee_v2 import *

pracownicy = wczytaj_pracownikow('pracownicy.csv')
print(f'Wczytano {len(pracownicy)} rekordów:')
for p in pracownicy:
    print(p)
