# W tej wersji używamy dodatkowego modułu requests, który został doinstalowany: pip install requests
import requests

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'

try:
    print('Pobieram dane...')
    dane = requests.get(ADRES).json()
    tabela = dane[0]
    print('Tabela numer', tabela['no'], 'z dnia', tabela['effectiveDate'])

    waluty = tabela['rates']
    for waluta in waluty:
        print(waluta['code'], waluta['currency'], waluta['mid'])

except Exception as e:
    print('Nie udało się pobrać', e)
