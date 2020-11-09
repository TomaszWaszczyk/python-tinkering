def oblicz(x, y, op):
    # teraz nie da rady: print('Mam dostęp do zmiennych globalnych:', liczba1)
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
        raise ValueError(f'Nieznana operacja {op}')


def main():
    try:
        liczba1 = int(input('Podaj pierwszą liczbę: '))
        liczba2 = int(input('Podaj drugą liczbę: '))
        operacja = input('Podaj rodzaj operacji: ')
        wynik = oblicz(liczba1, liczba2, operacja)
        print('Wynik:', wynik)
    except ZeroDivisionError:
        print('Próba dzielenia przez zero!')
    except Exception as e:
        # To wyłapie resztę wyjątków
        print('Wystąpił błąd:', type(e), e)
    print('Koniec programu')


# Zamknięcie programu w funkcji main powoduje, że zmienne nie są globalne, tylko lokalne.
# Taki if zapobiega wykonaniu treści tego pliku gdy jest on importowany z innego pliku.
# Np. PyCharm traktuje tę linię jako "aktywator programu", pojawia się strzałka "Run"
if __name__ == '__main__':
    main()
