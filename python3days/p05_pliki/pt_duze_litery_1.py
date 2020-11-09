WEJSCIE = 'pan-tadeusz.txt'
WYJSCIE = 'duze1.txt'

# Podejście pierwsze - czytam cały plik do pamięci
# i zapisuję jako jednego wielkiego stringa

with open(WEJSCIE, mode='r', encoding='UTF-8') as wejscie:
    tekst = wejscie.read()

with open(WYJSCIE, mode='w', encoding='UTF-8') as wyjscie:
    wyjscie.write(tekst.upper())

print('Gotowe')
