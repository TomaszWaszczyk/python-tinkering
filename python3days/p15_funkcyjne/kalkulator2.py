# W tej wersji stosujemy zmienną wynik, aby uniknąć duplikacji kodu wypisującego wynik
# Ignoruję problem dzielenia przez 0.

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

if op == '+':
    wynik = x+y
elif op == '-':
    wynik = x-y
elif op == '*':
    wynik = x*y
elif op == '/':
    wynik = x/y
elif op == '^':
    wynik = x**y
else:
    # W Pythonie zmienne nie mają określonego typu i można zrobić taką (mało elegancką) rzecz:
    wynik = 'Nieznana operacja ' + op

print('Wynik:', wynik)
