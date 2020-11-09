WEJSCIE = 'pan-tadeusz.txt'
WYJSCIE = 'duze2.txt'

# Tutaj jeszcze with

with open(WEJSCIE, mode='r', encoding='UTF-8') as wejscie,\
     open(WYJSCIE, mode='w', encoding='UTF-8') as wyjscie:
    for linia in wejscie:
        wyjscie.write(linia.upper())

print('Gotowe')
