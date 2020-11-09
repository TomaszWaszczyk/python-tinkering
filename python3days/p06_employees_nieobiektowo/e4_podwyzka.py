from decimal import Decimal

# 4) Zapytaj o nazwę stanowiska oraz o zmianę pensji i DO NOWEGO PLIKU zapisz dane z uwględnioną "podwyżką" dla danego stanowiska
kogo_szukam = input('Podaj nazwę stanowiska: ')
podwyzka = Decimal(input('Podaj kwotę podwyżki: '))

with open('pracownicy.csv', mode='r', encoding='UTF-8') as plik,\
     open('podwyzka.csv', mode='w', encoding='UTF-8') as wyjscie:
    ile = 0
    for linia in plik:
        t = linia.strip().split(';')
        if t[3] == kogo_szukam:
            ile += 1
            salary = Decimal(t[4])
            salary += podwyzka
            t[4] = str(salary)
            # albo zwięźlej: t[4] = str(Decimal(t[4]) + podwyzka)

        # dwa sposoby wypisywania wielu pól w jednej linii:
        # print(';'.join(t), file=wyjscie)
        print(*t, sep=';', file=wyjscie)

    print(f'Zmieniono {ile} rekordów')
