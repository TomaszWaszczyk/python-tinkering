from employee_v2 import *

pracownicy = wczytaj_pracownikow('../pracownicy.csv')

ilosc = {p.job_title: 0 for p in pracownicy}
suma = {p.job_title: 0 for p in pracownicy}

for p in pracownicy:
    ilosc[p.job_title] += 1
    suma[p.job_title] += p.salary


for job in ilosc.keys():
    srednia = suma[job] / ilosc[job]
    print(f'{job:32} {ilosc[job]:2} {srednia:10.2f}')
