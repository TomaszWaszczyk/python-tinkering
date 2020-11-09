# Używamy dwóch modułów ze standardowej biblioteki Pythona
import json
from urllib import request

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'

print('Pobieram dane...')

# Bez żadnych dodatkowych bibliotek można pobrać dane z sieci i potraktować jak JSON-a w taki sposób:
with request.urlopen(ADRES) as response:
    txt = response.read().decode('utf-8')

dane = json.loads(txt)
print(type(dane))

tabela = dane[0]
print(type(tabela))
print()

print('Tabela numer', tabela['no'], 'z dnia', tabela['effectiveDate'])
print()

waluty = tabela['rates']

print('Wszystkie waluty:')
for waluta in waluty:
    print(waluta['code'], waluta['currency'], waluta['mid'])


