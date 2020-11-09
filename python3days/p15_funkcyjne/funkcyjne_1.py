def zrob_cos():
    print('Robię coś')
    print('lalalala')
    print()

def zrob_cos_innego():
    print('Robię coś innego')
    print('gagagaga')
    print()


# W Pythonie funkcję można wpisać na zmienną, przekazać jako parametr, zapamiętać w kolekcji...
# "Funkcja też jest wartością"
print('Zaraz na zmienną wpiszę sobie funkcję...')
funkcja = zrob_cos
print('Funkcja przypisana:', funkcja)

print('Dopiero teraz uruchomię funkcję 3 razy:')
for i in range(3):
    funkcja()
print('Gotowe')
print()

lista_funkcji = [zrob_cos, zrob_cos_innego]
print(lista_funkcji)

for f in lista_funkcji:
    f()

print()

# Funkcja wyższego rzędu to taka funkcja, któ©a przyjmuje inną funkcję jako parametr:
def powtorz(funkcja, ile_razy=1):
    for i in range(ile_razy):
        funkcja()


powtorz(zrob_cos, 3)

powtorz(zrob_cos_innego, 5)

# Gdy jakaś funkcja oczekuje innej funkcji jako argumentu, to jako "inną funkcję" możemy przekazać wyrażenie lambda
powtorz(lambda: print('to jest lambda'), 4)

