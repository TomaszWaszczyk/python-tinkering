
plik = open('plik.txt')
print('Zmienna plik:', plik)

cala_tresc = plik.read()
print('Typ treści:', type(cala_tresc), len(cala_tresc), 'znaków')
print('Cała treść:')
print(cala_tresc)
plik.close()

print()

# Najbardziej typowy schemat czytania pliku tekstowego w Pythonie
#  * with - sposób na automatyczne zamykanie plików (bez jawnego pisania close, nawet w przypadku wyjątków)
#  * for - otwarty plik jest "iteratorem", czyli można pobierać z niego dane za pomocą pętli for
#    w przypadku pliku tekstowego pętla for czyta kolejne linie jako stringi

with open('plik.txt', mode='r', encoding='UTF-8') as plik:
    for linia in plik:
        print(linia)

# Wyjście z bloku with oznacza zamknięcie pliku
print('Plik jest znowu zamknięty')
