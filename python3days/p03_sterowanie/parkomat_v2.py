cena = 3

godziny = int(input('Ile godzin będziesz parkować: '))
do_zaplaty = godziny * cena
print(f'Do zapłaty {do_zaplaty} zł')

while do_zaplaty > 0:
    print(f'Do zapłaty pozostało {do_zaplaty} zł')
    moneta = int(input('Wrzuć monetę: '))
    do_zaplaty -= moneta

if do_zaplaty < 0:
    print(f'Należy się reszta w wysokości {-do_zaplaty} zł')

print('Dziękujemy')
