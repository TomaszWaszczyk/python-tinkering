# Dekorator to jest "funkcja na funkcjach"
def dekorator(funkcja):
    def zmieniona_funkcja():
        print('Zaraz uruchomię funkcję')
        wynik = funkcja()
        print('Funkcja się zakończyła i dała w wyniku', wynik, 'typu', type(wynik))
        return wynik

    return zmieniona_funkcja

# Gdy definiuję "normalną" funkcję, mogę ozdobić ją dekoratorem,
# i wtedy za każdym razem, gdy ktoś tę funkcję odpali, zostanie "opakowana" - zamiast niej zostanie wywołany "wrapper"

@dekorator
def aaa():
    print('aaa: Ala ma kota')
    return 'kot'


print('Początek programu')
w = aaa()
print('Wynikiem ostatecznym jest:', w)
print()


# Dodanie dekoratora przed funkcją aaa() działa tak, jak poniżej przekazanie funkcji bbb() do dekoratora jako parametru

def bbb():
    print('Basia ma rybkę')
    return 'rybka'

zmienione_bbb = dekorator(bbb)
w = zmienione_bbb()
print('Wynikiem ostatecznym jest:', w)
print()


@dekorator
def ccc():
    print('ccc: Celina ma chomika')
    return 'chomik'


ccc()
ccc()
