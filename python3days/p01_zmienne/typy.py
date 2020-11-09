# Typy danych:
# int - liczba całkowita
x = 15
y = 20
z = -6
print(type(x), x)
print(x + y)
print(x * 2)

# W Pythonie liczby całkowite nie mają ograniczenia na wielkość,
# a obliczenia na int-ach zawsze są w pełni precyzyjne.
print(x ** y)
print()

# float - liczba z ułamkiem, "zmiennoprzecinkowa", odpowiednik double z języków C, Java
f = 3.14
print(type(f), f)
# zalety: można obsługiwać zarówno bardzo duże, jak i bardzo małe wartości

f = 1.2e40  # oznacza 1.2 * (10 do potęgi 40)
print(f)

f = 1.2e-20
print(f)

f = 3.14e2
print(f)

# ilość znaczących cyfr jest ograniczona - float musi zmieścicsięw 64 bitach pamięci
# w dodatku komputer przechowuje te dane w systemie dwójkowym (jako ułamki / potęgi liczby 2)

f = 1.2
print(3 * f)
print(3 * 1.2)

# Szczególnie groźne jest porónywanie wyników na zasadzie "musi być dokładnie równe"
if 3*f == 3.6:
    print('TAK')
else:
    print('NIE')

# float (czasami nazywane też double albo real - upraszczając trochę)
# jest rzeczą znaną z innych języków programowania - i w nich mamy ten sam problem
# po prostu procesory tak działają

# w razie potrrzeby precyzyjnych obliczeń z ułamkami (np. księgowość itp.)
# można użyć typu Decimal - wymaga importu i odpowiedniego użycia

print()

# str - napis
# w większości innych języków nazywa się string
s = 'Ala ma kota'
t = ' a Ola ma psa'
print(type(s), s)
if isinstance(s, str):
    print('Tak, to jest napis')
else:
    print('Nie, to nie jest napis')

print(s + t)
print(s * 2)
# print(s - t)

# Można wybierać pojedyncze znaki lub fragmenty:
print(s[0])
print(s[4:6]) # od włącznie do wyłączając, numeracja od zera

# Typ decyduje o tym, co można z daną wartością robić i jak działają określone operacje.

liczba = 1234
# print(liczba[0])

# można konwertować wartości między typami
napis = str(liczba)
print(napis)
print(napis[0]) # teraz OK

napis_z_liczba = '4321'
# to jest napis, np napis_z_liczba * 2 dałoby '43214321'
print(napis_z_liczba * 2)

# z takiego napisu można utworzyć liczbę za pomocą takiej konwersji (mówi się też "rzutowania")
x = int(napis_z_liczba)
print(x)
print(x * 2)
print()

# bool - typ dla wartości logicznych
# b = True
# b = False
b = x > 500
print(type(b), b)
if b:
    print('PRAWDA')
else:
    print('FAŁSZ')


print()
lista = [123, 456, 'Ala', 'kot']

print(type(lista), lista)
print(lista[1])

