"""
Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:
formatuj(
    'koszt $cena PLN przy stawce VAT $vat%',
    'kwota $cena brutto',
    cena=10,
    vat=23,
)
'koszt 10 PLN przy stawce VAT 23%\nkwota 10 brutto'
"""
# Podpowiedzi:
# s = 'Ala ma kota i także ma psa.'
# wynik = s.replace('ma', 'posiada')
# print(wynik)
#
# t = ['Ala', 'Ola', 'Ela']
# wynik = '; '.join(t)
# print(wynik)


def formatuj(*args, **kwargs):
    tekst = '\n'.join(args)
    for k, v in kwargs.items():
        tekst = tekst.replace('$'+k, str(v))
    return tekst

txt = formatuj('koszt towaru $towar $cena PLN przy stawce VAT $vat%', 'kwota $cena brutto',
               cena=10, vat=23, towar='pomidor')
print(txt)
