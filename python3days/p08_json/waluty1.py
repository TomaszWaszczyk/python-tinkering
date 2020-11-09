''' Przykładowe adresy
http://api.nbp.pl/api/exchangerates/tables/A
http://api.nbp.pl/api/exchangerates/tables/B
http://api.nbp.pl/api/exchangerates/tables/C
http://api.nbp.pl/api/exchangerates/tables/A/2015-05-05

http://api.nbp.pl/api/exchangerates/tables/A?format=xml
http://api.nbp.pl/api/exchangerates/tables/A?format=json
'''

# na zmienną wrzucam to, co pobrałem z serwisu NBP
json = [{"table": "A", "no": "104/A/NBP/2020", "effectiveDate": "2020-05-29",
         "rates": [{"currency": "bat (Tajlandia)", "code": "THB", "mid": 0.1258},
                   {"currency": "dolar amerykański", "code": "USD", "mid": 4.0031},
                   {"currency": "dolar australijski", "code": "AUD", "mid": 2.6614},
                   {"currency": "dolar Hongkongu", "code": "HKD", "mid": 0.5164},
                   {"currency": "dolar kanadyjski", "code": "CAD", "mid": 2.9064},
                   {"currency": "dolar nowozelandzki", "code": "NZD", "mid": 2.4825},
                   {"currency": "dolar singapurski", "code": "SGD", "mid": 2.8349},
                   {"currency": "euro", "code": "EUR", "mid": 4.4503},
                   {"currency": "forint (Węgry)", "code": "HUF", "mid": 0.012775},
                   {"currency": "frank szwajcarski", "code": "CHF", "mid": 4.1621},
                   {"currency": "funt szterling", "code": "GBP", "mid": 4.9213},
                   {"currency": "hrywna (Ukraina)", "code": "UAH", "mid": 0.1489},
                   {"currency": "jen (Japonia)", "code": "JPY", "mid": 0.037332},
                   {"currency": "korona czeska", "code": "CZK", "mid": 0.1649},
                   {"currency": "korona duńska", "code": "DKK", "mid": 0.5970},
                   {"currency": "korona islandzka", "code": "ISK", "mid": 0.029511},
                   {"currency": "korona norweska", "code": "NOK", "mid": 0.4108},
                   {"currency": "korona szwedzka", "code": "SEK", "mid": 0.4233},
                   {"currency": "kuna (Chorwacja)", "code": "HRK", "mid": 0.5864},
                   {"currency": "lej rumuński", "code": "RON", "mid": 0.9186},
                   {"currency": "lew (Bułgaria)", "code": "BGN", "mid": 2.2754},
                   {"currency": "lira turecka", "code": "TRY", "mid": 0.5867},
                   {"currency": "nowy izraelski szekel", "code": "ILS", "mid": 1.1408},
                   {"currency": "peso chilijskie", "code": "CLP", "mid": 0.004951},
                   {"currency": "peso filipińskie", "code": "PHP", "mid": 0.0793},
                   {"currency": "peso meksykańskie", "code": "MXN", "mid": 0.1803},
                   {"currency": "rand (Republika Południowej Afryki)", "code": "ZAR", "mid": 0.2281},
                   {"currency": "real (Brazylia)", "code": "BRL", "mid": 0.7407},
                   {"currency": "ringgit (Malezja)", "code": "MYR", "mid": 0.9213},
                   {"currency": "rubel rosyjski", "code": "RUB", "mid": 0.0566},
                   {"currency": "rupia indonezyjska", "code": "IDR", "mid": 0.00027403},
                   {"currency": "rupia indyjska", "code": "INR", "mid": 0.053021},
                   {"currency": "won południowokoreański", "code": "KRW", "mid": 0.003236},
                   {"currency": "yuan renminbi (Chiny)", "code": "CNY", "mid": 0.5605},
                   {"currency": "SDR (MFW)", "code": "XDR", "mid": 5.5167}]}]

# to jest lista jednoelementowa
print('json', type(json), len(json))

# pojedyncze tabele są słownikami
tabela = json[0]
print('tabela', type(tabela), len(tabela))

# Pod kluczem 'rates' znajduje się lista 35 walut
rates = tabela["rates"]
print('rates', type(rates), len(rates))

waluta = rates[1]
print('waluta', type(waluta), len(waluta))

print(waluta["code"], waluta["mid"])

print('Kurs dolara:', json[0]["rates"][1]["mid"])

print()

print('Wszystkie waluty:')
for waluta in rates:
    print(waluta)
print()

for waluta in rates:
    kod = waluta["code"]
    nazwa = waluta["currency"]
    kurs = waluta["mid"]
    print(f'{kod} {"("+nazwa+")":40} : {kurs:<8}')
