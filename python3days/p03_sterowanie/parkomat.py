# Godzina parkowania kosztuje 3 zł

# Program pyta "Ile godzin będziesz parkować?"
# Program oblicza i wypisuje ile będzie do zapłaty.

# W pętli program prosi o wrzucenie kolejnej monety
# aż zbierze się wymagana kwota.
# "Wrzucenie monety" to po prostu wpisanie liczby (użyć input).

# Jak już zbierze się wymagana kwota, to sprawdza czy należy się reszta i ew. ją wydaje.

cena = 3

godziny = int(input('Ile godzin będziesz parkować: '))
do_zaplaty = godziny * cena
print(f'Do zapłaty {do_zaplaty} zł')

suma_wplat = 0

while suma_wplat < do_zaplaty:
    print(f'Do tej pory wpłacono {suma_wplat}, do zapłaty pozostało {do_zaplaty - suma_wplat} zł')
    moneta = int(input('Wrzuć monetę: '))
    suma_wplat += moneta

if suma_wplat > do_zaplaty:
    print(f'Należy się reszta w wysokości {suma_wplat - do_zaplaty} zł')

print('Dziękujemy')
