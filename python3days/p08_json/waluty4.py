# W tej wersji używamy dodatkowego modułu requests, który został doinstalowany: pip install requests
import requests

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'
try:
    print('Pobieram dane...')
    dane = requests.get(ADRES).json()
    tabela = dane[0]
    print('Tabela numer', tabela['no'], 'z dnia', tabela['effectiveDate'])
    waluty = tabela['rates']

    szukana_waluta = input('Podaj kod waluty: ').upper()
    kwota = float(input('Podaj kwotę: '))

    for waluta in waluty:
        if waluta['code'] == szukana_waluta:
            kod = waluta['code']
            nazwa = waluta['currency']
            kurs = waluta['mid']

            print(f'Waluta {nazwa} (kod {kod}) ma kurs {kurs}')
            kwotaZlote = kwota * kurs
            print(f'{kwota:.2f} {kod} = {kwotaZlote:.2f} PLN')
            kwotaWaluta = kwota / kurs
            print(f'{kwota:.2f} PLN = {kwotaWaluta:.2f} {kod}')
            break
    else:
        print(f'Nie ma takiej waluty {szukana_waluta}')

except Exception as e:
    print('Nie udało się pobrać', e)
