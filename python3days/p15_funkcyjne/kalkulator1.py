# Napisz program, który na podstawie dwóch podanych liczb obliczy
# wynik zadanej operacji (dodawanie, odejmowanie, mnożenie,
# dzielenie). W przypadku podania nieprawidłowej operacji program
# ma wyświetlić odpowiedni komunikat o błędzie.

# Przykładowy komunikat programu:
# Podaj pierwszą liczbę: 10
# Podaj drugą liczbę: 5
# Podaj rodzaj operacji: +
# Wynik: 15

x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
op = input('Podaj rodzaj operacji: ')

if op == '+':
    print('Wynik:', x+y)
elif op == '-':
    print('Wynik:', x-y)
elif op == '*':
    print('Wynik:', x*y)
elif op == '/':
    if y == 0:
        print('Nie dzielimy przez zero')
    elif x % y == 0:
        print('Wynik:', x // y)
    else:
        print('Wynik:', x / y)
elif op == '^':
    print('Wynik:', x**y)
else:
    print('Nieznana operacja', op)

