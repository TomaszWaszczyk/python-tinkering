from employee_v2 import *

pracownicy = wczytaj_pracownikow('../pracownicy.csv')

slownik = {}
# W tej wersji w slowniku będę pamiętał listy dwuelementowe,
# z ilością i sumą.
# {'Programmer': [5, 27800], 'President': [1, 24000], ...}

for p in pracownicy:
    if p.job_title not in slownik:
        slownik[p.job_title] = [1, p.salary]
    else:
        slownik[p.job_title][0] += 1
        slownik[p.job_title][1] += p.salary


# for job in slownik.keys():
#     srednia = slownik[job][1] / slownik[job][0]
#     print(f'{job:32} {slownik[job][0]:2} {srednia:10.2f}')

# Tutaj zastosujemy unpacking
# Pojedynczy item to coś takiego: ('Programmer', [5, 28800])
for (job, [ilosc, suma]) in slownik.items():
    srednia = suma / ilosc
    print(f'{job:32} {ilosc:2} {srednia:10.2f}')

