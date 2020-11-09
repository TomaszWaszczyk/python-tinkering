from employee_v2 import *

pracownicy = wczytaj_pracownikow('../pracownicy.csv')

ilosc = {}
suma = {}
for p in pracownicy:
    if p.job_title not in ilosc:
        ilosc[p.job_title] = 1
        suma[p.job_title] = p.salary
    else:
        ilosc[p.job_title] += 1
        suma[p.job_title] += p.salary


for job in ilosc.keys():
    srednia = suma[job] / ilosc[job]
    print(f'{job:32} {ilosc[job]:2} {srednia:10.2f}')
