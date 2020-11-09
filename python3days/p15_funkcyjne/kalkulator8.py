operacje = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
    '%': lambda x,y: x%y,
    '^': lambda x,y: x**y, # potęgowanie
}


def oblicz(x, y, symbol):
    if symbol in operacje:
        funkcja = operacje[symbol]
        return funkcja(x, y)
    else:
        raise ValueError(f'Nieznana operacja {symbol}')


def main():
    try:
        x = int(input('Podaj 1. liczbę: '))
        y = int(input('Podaj 2. liczbę: '))
        symbol = input('Podaj znak operacji: ')
        wynik = oblicz(x, y, symbol)
        print('Wynikiem jest:', wynik)
    except Exception as e:
        print(f'Nastąpił błąd typu {type(e)}: {e}')


if __name__ == '__main__':
    main()
