# W standardowej bibliotece Pythona (bez żadnego pip install)
# mamy dostępny moduł urllib.request, który oferuje podstawowe, ale niezby wygodne wsparcie dla zapytań HTTP

from urllib import request

ADRES = 'http://students.alx.pl/~pczarnik/alx-pyt-12-maj/zadania_domowe_2.pdf'

response = request.urlopen(ADRES)
print(response)
print('kod', response.getcode())
print('info', response.info())

dane = response.read()

with open('plik.pdf', mode='wb') as wynikowy:
    wynikowy.write(dane)

print('gotowe')


