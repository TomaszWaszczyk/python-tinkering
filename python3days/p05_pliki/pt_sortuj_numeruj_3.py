import locale

print('czytanie...')
with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
    linie = plik.readlines()

print('Ilość linii:', len(linie))

linie = [linia2 for linia2 in (linia.strip() for linia in linie) if linia2]
# alternatywnie: użyć funkcji filter i map
# linie = list(filter(lambda s: len(s) > 0, map(str.strip, linie)))

print('Ilość niepustych linii:', len(linie))

print('sortowanie...')
locale.setlocale(locale.LC_ALL, '')
linie.sort(key=locale.strxfrm)
print('zapis...')

with open('posortowany3.txt', mode='w', encoding='utf-8') as plik:
    for nr, linia in enumerate(linie):
        print(f'{nr+1:5}: {linia}', file=plik)

print('gotowe')
