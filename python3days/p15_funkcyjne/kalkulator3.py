def oblicz(x, y, op):
    print('Mam dostęp do zmiennych globalnych:', liczba1) # to wcale nie jest dobrze
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    elif op == '^':
        return x ** y
    else:
        return None


liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji: ')

wynik = oblicz(liczba1, liczba2, operacja)
if wynik is None:
    print('Brak wyniku')
else:
    print('Wynik:', wynik)
