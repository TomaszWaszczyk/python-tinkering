# Napisz program, który symuluje w trybie tekstowym obsługę klienta w sklepie.
# Program w pętli pozwala podać nazwę oraz ilość towaru. (np. klient moż kupić 2 praki i odkurzacz)
# Wprowadzanie danych kończymy pustym stringiem

# Program na końcu wypisuje sumę do zapłaty za wszystko
# Fajnie by było, gdyby program był odbporny na błędy io np. dla nieistniejącego towaru wypisywał komunikat, ale działał dalej

# 1) Program wypisuje cennik
# 2) Podaj nazwę towaru: pralka    (puste oznacza koniec)
# 3) Podaj ilość: 2
# goto 2)

# 4) Za wszsytko zapłacisz 1240

cennik = {
    'pralka': 2800,
    'odkurzacz': 690,
    'kuchenka': 3500,
}

for towar, cena in cennik.items():
    print(f' * {towar:12} za {cena:5} zł')
print()

suma = 0
while True:
    towar = input('Podaj nazwę towaru (puste aby zakończyć)?: ')
    if not towar:
        break # jeśli str jest pusty
    if towar not in cennik:
        print('Nie ma takiego towaru')
        continue
    # nie muszę pisać else
    ilosc = int(input('Ile sztuk?: '))
    do_zaplaty = ilosc * cennik[towar]
    suma += do_zaplaty
    print(f'Za {ilosc} sztuk towaru {towar} zapłacisz {do_zaplaty} zł')

print(f'Za wszystkie towary łącznie zapłacisz {suma} zł')
