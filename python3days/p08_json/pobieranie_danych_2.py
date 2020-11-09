
import requests

ADRES = 'http://students.alx.pl/~pczarnik/alx-pyt-12-maj/zadania_domowe_2.pdf'

response = requests.get(ADRES)

print(response)
print('kod', response.status_code)
dane = response.content

with open('plik2.pdf', mode='wb') as wynikowy:
    wynikowy.write(dane)

print('gotowe')

