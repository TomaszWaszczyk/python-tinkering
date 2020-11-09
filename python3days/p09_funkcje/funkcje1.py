print('To jest pierwsza normalna programu')

# Definicja funkcji:
def aaa():
    print('AAA kotki dwa')
    print('Ala ma kota')

def nieistotna():
    print('To się nigdy nie wypisze')
    print('Ani to')

# Zdefiniowanie funkcji nie oznacza jeszcze jej wykonanaia.
print('To jest druga normalna programu')
print()

# Wywołanie funkcji (call / invoke)
aaa()
print('Chwilka przerwy...')
aaa()
print()

# Funkcje mogą mieć parametry
# W Pythonie parametry mogą mieć wartości domyślne (inaczej): niektóre parametry mogą być opcjonalne)
def powtorz(napis, ile_razy=1):
    for i in range(ile_razy):
        print(napis)
    print()

powtorz('Ola ma psa', 3)
powtorz('Ela ma chomika', 5)
powtorz('Ala ma kota') # 1 raz

# Funkcje mogą zwracać wynik
def ostatnia_cyfra(liczba):
    return liczba % 10

# Jeśli wywołam funkcję zwracającą wynik, to mogę ten wynik zapisać na zmienną
wynik = ostatnia_cyfra(113)
print('Ostatnia cyfra ze 113:', wynik)

# Można też użyć w dowolnym kontekście, gdzie oczekiwana jest wartość:
print(ostatnia_cyfra(1007)) # 7
print(500 + ostatnia_cyfra(44) + 1000)  # 1504

# Można też wywołać funkcję, która zwraca wynik, ale w ogóle z tym wynikiem nic nie robić
### !!! return to nie to samo co print !!! ###
ostatnia_cyfra(999) # 9 nigdzie się nie wypisze
print('Koniec z cyframi')
print()

# Najbardziej typowa funckcja matematyczna:

def do_kwadratu(x):
    return x ** 2

def pierwiastek(x):
    return x ** 0.5

print(do_kwadratu(5))
print(do_kwadratu(7))
print()
print(pierwiastek(25))
print(pierwiastek(2))
