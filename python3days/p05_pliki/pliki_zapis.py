# Zapisywanie plików

# Otwarcie pliku w trybie do zapisu
# Plik jest albo tworzony, albo zamazywany jeśli już był.
plik1 = open('wynik1.txt', 'w')
plik1.write('Pierwszy tekst.')
plik1.write('Drugi tekst.')
# Oba teksty połączą się w jedną linię.
# Aby w ten sposób zapisać osobną linię, dodajemy \n.

plik1.write('Koniec.\n')
plik1.write('Druga linia\n')
plik1.close()

linie = ['Ala ma kota\n', 'Ola ma psa\n', 'Ela ma chomika\n']

# Dzięki with plik sam się zamknie
with open(file='wynik2.txt', mode='w', encoding='UTF-8') as plik2:
    # write zapisuje jeden napis
    plik2.write('Pierwsza linia\n')

    # writelines zapisuje wiele tekstów
    plik2.writelines(linie)

    # można też użyć print z parametrem file
    print('To napisał print.', file=plik2)
    print('Ala', 'ma', 'kota', sep=';', file=plik2)

print('Koniec')
