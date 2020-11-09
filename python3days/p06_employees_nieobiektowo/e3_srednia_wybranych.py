# 3) Zapytaj o nazwę stanowiska (np. Programmer) i oblicz liczbę oraz średnią pensję takich pracowników.

kogo_szukam = input('Podaj nazwę stanowiska: ')

suma = 0
ilosc = 0
with open('pracownicy.csv', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        t = linia.split(';')
        if t[3] == kogo_szukam:
            suma += float(t[4])
            ilosc += 1

if ilosc == 0:
    print('Nie takich ludzików')
else:
    srednia = suma / ilosc
    print(srednia)

# 4) Zapytaj o nazwę stanowiska oraz o zmianę pensji i DO NOWEGO PLIKU zapisz dane z uwględnioną "podwyżką" dla danego stanowiska
