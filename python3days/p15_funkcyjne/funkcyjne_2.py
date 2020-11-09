def do_kwadratu(a):
    return a*a

def razy_dziesiec(x):
    return 10*x

# W Pythonie funkcję można trakotwać jak wartość:
# zapisać na zmienną, przekazać jako parametr, przechowywać w kolekcjach

# Piszą nazwę funkcji bez nazwiasów nie wywołujemy jej, tylko "wskazujemy"
f = do_kwadratu

# Teraz mogę wywołać funkcję uzywając nazwy f:
wynik = f(5) # 25
print(wynik)

f = razy_dziesiec
wynik = f(5) # 50
print(wynik)

# Wyrażenie lambda to jest sposób na zwięzłe zdefiniowanie funkcji bez podawania jej nazwy
# na zmienną f wpisuję funkcję, która zwieksza parametr o 1
f = lambda x: x+1
wynik = f(5)
print(wynik)
print()

# Funkcje mogą być też parametrami innych funkcji
def powtorz(instrukcja, ile_razy=1, *args):
    for i in range(ile_razy):
        instrukcja(*args) # nawiasy oznaczają, że w tym momencie wywołuję (uruchamiam) funkcję


def aaa():
    print('Ala ma kota')
    print('  i co z tego?')


def bbb(kto, co):
    print(f'{kto} ma {co}')


print('AAAAAAA')
powtorz(aaa, 5)
print('\nBBBBBBBBBBBB\n')
powtorz(bbb, 3, 'Ola', 'psa')


print('\nCCC\n')
powtorz(lambda : print('Celina ma chomika'), 3)
print()

liczby = [10, 20, 30, 40, 50]
lista_funkcji = [lambda x: x, do_kwadratu, razy_dziesiec, lambda x: x-1]

for liczba in liczby:
    for funkcja in lista_funkcji:
        print(funkcja(liczba), end=', ')
    print()
