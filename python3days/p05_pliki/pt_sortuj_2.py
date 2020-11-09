import locale

print('czytanie...')
with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
    linie = plik.readlines()

print('Ilość linii:', len(linie))
print('sortowanie...')
locale.setlocale(locale.LC_ALL, '')
linie.sort(key=locale.strxfrm)
print('zapis...')

with open('posortowany.txt', mode='w', encoding='utf-8') as plik:
    plik.writelines(linie)

print('gotowe')
