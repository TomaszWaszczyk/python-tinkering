print('czytanie...')

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
    linie = plik.readlines()

print('Ilość linii:', len(linie))
print('sortowanie...')
linie.sort()
print('Posortowane:')

for linia in linie:
    print(linia, end='')
