# silnia(5) = 1*2*3*4*5 = 120
def silnia(n):
    iloczyn = 1
    for i in range(2, n+1):
        iloczyn *= i
    return iloczyn


def main():
    while True:
        s = input('Podaj liczbę (puste aby zakończyć)\n')
        if not s: break
        try:
            n = int(s)
            wynik = silnia(n)
            print(f'{n}! = {wynik}')
        except Exception as e:
            print('Błąd:', e)


if __name__ == '__main__':
    main()
