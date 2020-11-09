# Różne sposoby wypisywania danych w Pythonie:

x = 123
y = 3
wynik = x * y

print(wynik)

# print pozwala wypisać kilka rzeczy na raz, podczas wypisywania rozdziela je spacją
print('Wynik wynosi', wynik)

print(x, 'razy', y, 'jest równe', x*y)
print()


# Aby odstępem nie była spacja, tylko coś innego, może podać parametr sep

print('Ala', 'Ola', 'Ela') # rozdziela spacjami

print('Adam', 'Tomasz', 'Andrzej', sep=' oraz ') # rozdziela słowem oraz
print('Ala', 'Ola', 'Ela', 'Ula', sep=';')
print(12, 13, 14, 15, sep='')
print()

# Aby print nie przechodził do nowej linii, można ustawić pusty parametr end

print('Ala ma kota', end='')
print('Ola', 'ma', 'psa', end='!')
print('Koniec')
print()

# Sposoby na łączenie fragmentów tekstu z wartościami

# 1) Podejście klasyczne: operator % ("modulo"). Analogia do funkcji printf z języka C:
# Bardzo popularne w Pythonie 2 i ogólnie w starych programach Pythona
print('%d razy %d jest równe %d' % (x, y, wynik))
# d jest od decimal, a inne formaty to np. x - hexcadecimal, s - string, f - float

imie = 'Alicja'
pi = 3.14159
print('%s ma %f kotów, a %d szestastkowo zapisuje się jako %x' % (imie, pi, x, x))
print()

# 2) Funkcja format - coś pośredniego między 1) a 3), mi osobiście niezbyt się podoba
print('{} razy {} jest równe {}'.format(x, y, x*y))

# 3) f-string, dostępne od Pythona 3.6:
print(f'{x} razy {y} jest równe {wynik}')
print(f'{x} razy {y} jest równe {x*y}')
print()


# dodatkowa możliwości:
# wyrównywanie do określonej liczby pozycji
imie1 = 'Ala'
imie2 = 'Ewelina'
imie3 = 'Aleksandrowska'

print(imie1, 'ma kota')
print(imie2, 'ma kota')
print()
print('%10s ma kota' % imie1)
print('%10s ma kota' % imie2)
print('%-10s ma kota' % imie2)
print('%10s ma kota' % imie3)
print()
print('{:10} ma kota'.format(imie1))
print('{:10} ma kota'.format(imie2))
print('{:>10} ma kota'.format(imie2))
print('{:10} ma kota'.format(imie3))
print()
print(f'{imie1:10} ma kota')
print(f'{imie2:10} ma kota')
print(f'{imie2:>10} ma kota')
print(f'{imie3:10} ma kota')
print()

# zaokrąglanie do określonej liczby miejsc po przecinku
import math
p = math.sqrt(2)
print('pierwiastek:', p)

print('pierwiastek: %.3f' % p)
print('pierwiastek: {:.3f}'.format(p))
print(f'pierwiastek: {p:.3f}')

# Gdybym szerokość lub precyzję chciał wczytać ze zmiennej, to można tak:
precyzja = 6
print(f'pierwiastek: {p:.{precyzja}f}')
