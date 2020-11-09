slowo = input('Podaj szukane słowo: ')

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
    ile = 0
    for linia in plik:
        if slowo in linia:
            print(linia, end='')
            ile += 1

    print(f'\nZnaleziono {ile} linii')
