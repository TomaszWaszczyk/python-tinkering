# 2) Oblicz średnią pensję wszystkich

suma = 0
ilosc = 0
with open('pracownicy.csv', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        t = linia.split(';')
        suma += float(t[4])
        ilosc += 1

srednia = suma / ilosc
print(srednia)
