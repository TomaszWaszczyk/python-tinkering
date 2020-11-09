# Program zadaje pytanie "Co chcesz kupić?"
# przykładowa odpowiedź: telefon
# pytanie: "Ile kosztuje jedna sztuka telefon?"
# przykładowa odpowiedź: 1200
# "Ile sztuk telefon chcesz kupić?"
# przykładowa odpowiedź: 3
# Program wypisuje: "Za 3 sztuk towaru telefon zapłacisz 3600.00 zł"

from decimal import Decimal

towar = input('Co chcesz kupić? ')
cena = Decimal(input(f'Ile kosztuje jedna sztuka {towar}? '))
ilosc = int(input(f'Ile sztuk towaru {towar} chcesz kupić? '))

kwota = cena * ilosc

print(f'Za {ilosc} sztuk towaru {towar} zapłacisz {kwota} zł')
print(f'Za {ilosc} sztuk towaru {towar} zapłacisz {kwota:.2f} zł')
