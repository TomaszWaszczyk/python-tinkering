def pomnoz_przez_10(x):
    return 10*x


def ostatnie_slowo(tekst):
    kawalki = tekst.split()
    if len(kawalki) == 0:
        return ''
    else:
        return kawalki[-1]


# TODO Niech funkcja zwraca dłuższy z dwóch podanych napisów. Jeśli są równie długie, to pierwszy
def dluzszy_napis(napis1, napis2):
    if len(napis1) >= len(napis2):
        return napis1
    else:
        return napis2


def dluzszy_napis_v2(napis1, napis2):
    return napis1 if len(napis1) >= len(napis2) else napis2
    # dla znających C/Java
    # return len(napis1) >= len(napis2) ? napis1 : napis2


# TODO Napisz funkcję, która dla podanej liczby całkowitej oblicza sumę jej cyfr
def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = liczba // 10     # liczba =// 10
    return suma


def suma_cyfr_v2(liczba):
    return sum(int(c) for c in list(str(liczba)))


# właściwy program
wynik = pomnoz_przez_10(13)
if wynik > 100:
    print(f'wynik {wynik} jest większy niż 100')
else:
    print('wynik jest mały')
print()

print(pomnoz_przez_10(77))
print(ostatnie_slowo('Ala ma kota'))
print(ostatnie_slowo('  '))
print(ostatnie_slowo('Ola ma psa.'))
print()

print(dluzszy_napis('abc', 'abcdefg'))
print(suma_cyfr(0))
print(suma_cyfr(7))
print(suma_cyfr(40))
print(suma_cyfr(43))
print(suma_cyfr(1234987650))
print()
print(suma_cyfr_v2(7))
print(suma_cyfr_v2(1234987650))
