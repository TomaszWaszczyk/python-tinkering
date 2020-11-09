import random

x = random.randint(-10, 110)
y = random.randint(-10, 110)

print('x:', x)
print('y:', y)
print('iloczyn:', x*y)
print()

if x > y:
    print('x jest większy')
    print('gratulacje dla x')

print('to już zawsze się wypisze')
print()

# 3 warianty if-a:

# 1) if bez elsa
if x == y:
    print('bingo! liczby są sobie równe')

# 2) if-else
# program na pewno wykona dokładnie jedną z tych dwóch gałęzi
if x < 10:
    print('x jest jednocyfrowy')
else:
    print('x ma więcej cyfr')

print()

# 3) if-elif-else
# Python sprawdza po kolei warunki logiczne i wykona pierwszą gałąź, przy której był prawdziwy warunewk logiczny (wtedy dalej już nie sprawdza)
# elif-ów może być dowolnie dużo
# na końcu po wszystkich może (ale nie musi) być else, który wykona się jeśli żaden z warunków nie był prawdziwy
if x < y:
    print('x jest mniejszy niż y')
elif x > y:
    print('x jest większy niż y')
else:
    print('x jest równy y')

print()


if x < 0:
    print('x jest ujemny')
elif x < 10:
    print('x jest jednocyfrowy')
elif x < 100:
    print('x jest dwucyfrowy')
elif x < 1000:
    print('x jest trzycyfrowy')
else:
    print('x jest bardzo duży')


print()

# warunki logiczne
# operatory porównania:
#  ==   !=    <   <=   >   >=


# przy okazji: pojedynczą instrukcję po if (itp. instrukcjach sterujących) można wpisać w jendej linii
if x <= 100: print('mieści się w 100')

if 0 <= y and y < 50:
    print('y mieści się w przedziale [0, 50)')

# W Pythonie w taki sposób można sprawdzać czy liczba mieści sie w zakresie:
if 0 <= y < 50:
    print('y mieści się w przedziale [0, 50)')

# Niektórzy "Pajtoniści" piszą też tak:
if y in range(0, 50):
    print('y mieści się w przedziale range [0, 50)')
# to też działa, ale sprawdziłem, że jest wolniejsze i działa tylko dla liczb całkowitych
# i generalnie range służy do czegoś innego


# spójniki logiczne: and or not
# zdecydowanie zalecane jest uzywanie operatorów pisanych słownie (and or),
# a nie znaczkowo (& i |)

if x > 50 and y > 50:
    print('obie liczby są > 50')

if x > 50 or y > 50:
    print('któraś z liczb jest > 50')
    # co najmniej jedna, ale być może obie

if not x >= 0:
    print('x jest ujemny - sprawdziłem w dziwny sposób')


# W Pythonie działają automatyczne konwersje danych różnych typów (liczba, napis) na wartość logiczną

napis = 'Ala ma kota'
if napis:
    print('napis nie jest pusty')
    
    
napis = ''
if napis:
    print('napis nie jest pusty') # to się nie wykona
else:
    print('napis 2 JEST pusty')

# reguły:
# liczba równa 0 ->  fałsz
# liczba inna niż 0 -> prawda
# pusty napis -> fałsz
# niepusty napis -> prawda     (np. napisy ' ', '0' są prawdą)
# pusta kolekcja -> fałsz
# niepusta kolekcja -> prawda
# None -> fałsz

lista = [False]

if lista:
    print('Prawdą jest :', lista)

napis1 = 'Ola'
napis2 = 'Olek'
if napis1 < napis2:
    print('Ola')

