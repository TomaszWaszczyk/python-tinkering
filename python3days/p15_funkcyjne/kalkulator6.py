dzialania = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
    '^': lambda x,y: x**y,
}

try:
    liczba1 = int(input('Podaj pierwszą liczbę: '))
    liczba2 = int(input('Podaj drugą liczbę: '))
    operacja = input('Podaj rodzaj operacji: ')

    dzialanie = dzialania[operacja]
    wynik = dzialanie(liczba1, liczba2)
    print('Wynik:', wynik)
except ZeroDivisionError:
    print('Próba dzielenia przez zero!')
except KeyError:
    print('Nieznana operacja', operacja)
except Exception as e:
    print('Inny błąd:', type(e), e)

print('Koniec programu')

