from employee_v2 import *

def wylicz_joba(pracownicy, job):
    suma = 0
    ilosc = 0
    for p in pracownicy:
        if p.job_title == job:
            suma += p.salary
            ilosc += 1
    srednia = suma / ilosc
    print(f'{job:32} {ilosc:2} {srednia:10.2f}')


def main():
    pracownicy = wczytaj_pracownikow('../pracownicy.csv')

    # jobs = set(p.job_title for p in pracownicy)
    jobs = {p.job_title for p in pracownicy}

    print(f'Wszystkie joby ({len(jobs)}):')

    for job in jobs:
        wylicz_joba(pracownicy, job)


if __name__ == '__main__':
    main()
