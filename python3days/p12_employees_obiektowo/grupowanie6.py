from employee_v2 import *
from collections import defaultdict

pracownicy = wczytaj_pracownikow('../pracownicy.csv')

# defaultdict to taka wersja słownika, w której w razie braku braku wartości, jest zwracana wartość domyślna
# dla typu int wartością domyślną jest 0
ilosc = defaultdict(int)
suma = defaultdict(int)

for p in pracownicy:
    ilosc[p.job_title] += 1
    suma[p.job_title] += p.salary


for job in ilosc.keys():
    srednia = suma[job] / ilosc[job]
    print(f'{job:32} {ilosc[job]:2} {srednia:10.2f}')

