# Napisz program zliczający liczbę znaków w podanym przez
# użytkownika napisie pomiędzy nawiasami <>.
# Ala ma <kota>, a kot ma Alę
# 4

napis = input('Wprowadź napis:\n')

# To jest moje ulubione rozwiązanie. W przypadku kilku fragmentów policzy sumę ich długości.
licznik = 0
jestem_pomiedzy_nawiasami = False
for znak in napis:
    if znak == '<':
        jestem_pomiedzy_nawiasami = True
    elif znak == '>':
        jestem_pomiedzy_nawiasami = False
    elif jestem_pomiedzy_nawiasami:
        licznik += 1

print('Wynik:', licznik)
print()

### Podejście z zapamiętywaniem pozycji. Obliczy długość pierwszego (jeśli dodamy break) lub ostatniego fragmentu. ###
# To jest trochę w stylu C
poczatek = koniec = 0
for i in range(len(napis)):
    if napis[i] == '<':
        poczatek = i
    elif napis[i] == '>':
        koniec = i

print('Początek to', poczatek)
print('Koniec to', koniec)
wynik = koniec - poczatek - 1
print('Wynik:', wynik)
print()

### Podobnie, ale z wykorzystaniem enumerate ###
poczatek = koniec = 0
for i, znak in enumerate(napis):
    if znak == '<':
        poczatek = i
    elif znak == '>':
        koniec = i

print('Początek to', poczatek)
print('Koniec to', koniec)
wynik = koniec - poczatek - 1
print('Wynik:', wynik)
print()

### Znalezienie pozycji za pomocą index lub find ###
poczatek = napis.find('<')
koniec = napis.find('>')
print('Początek to', poczatek)
print('Koniec to', koniec)
wynik = koniec - poczatek - 1
print('Wynik:', wynik)
print()

# Wyciąć fragment można, aby go sobie wyświetlić. Do samego liczenia długości nie jest to potrzebne.
fragment = napis[poczatek+1:koniec]
print('Fragment:', fragment)
print('A jego długość to', len(fragment))

