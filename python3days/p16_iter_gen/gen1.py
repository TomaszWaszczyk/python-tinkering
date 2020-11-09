dzisiaj = 'poniedziałek'

# yield umieszcza w kodzie w podobny sposób jak return
# ale yield nie kończy funkcji, tylko idzie dalej
# Jeśli w miejscu użycia tej funkcji będzie próba pobrania kolejnej wartości, to funkcja idzie dalej i zwraca wynik kolejnego
# yield.

def imiona():
    yield 'Ala'
    yield 'Ola'
    yield 'Ela'
    if dzisiaj == 'poniedziałek':
        yield 'Ula'
    else:
        yield 'Iza'

print('Startujemy')

# funkcja zwraca w wyniku generator
print(imiona())

print()

# Typowy sposób użycia generatora, to pobranie wszystkiech elementów (wszystkich wyników zwracanych przez yield)
# w pętli for
for imie in imiona():
    print(imie)

# Można też utworzyć listę czy inną kolekcję:

lista = list(imiona())
print(lista)

