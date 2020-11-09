# Wersja 3 z break - tylko informacyjnie, wg mnie 1 i 2 są lepsze

cena = 3

godziny = int(input('Ile godzin będziesz parkować: '))
do_zaplaty = godziny * cena
print(f'Do zapłaty {do_zaplaty} zł')

while True:
    print(f'Do zapłaty pozostało {do_zaplaty} zł')
    moneta = int(input('Wrzuć monetę: '))
    do_zaplaty -= moneta
    if do_zaplaty < 0:
        print(f'Należy się reszta w wysokości {-do_zaplaty} zł')
        break
    elif do_zaplaty == 0:
        print(f'Wpłacono co do grosza :-)')
        break

print('Dziękujemy')
