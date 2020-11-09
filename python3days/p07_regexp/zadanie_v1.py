import re

# Gdy używamy findall, a wzorzec zawiera nawiasy okrągłe,
# to findall z każdego dopasowania zwróci pierwszą grupę.
# Żeby nie traktował nawiasów okrągłych jak grup i żeby zwracał całe dopasowane napisy,
# trzeba grupy oznaczyć jako anonimowe (?: )
# W tym przypadku te nawiasy nie są jakoś krytycznie potrzebne, ale zostawiam taki przykład.
wzorzec_emaila = r'[A-Za-z0-9_.\-]+@(?:[A-Za-z0-9_\-]+\.)+[A-Za-z]+'

with open('re_teksty.txt') as plik:
    tekst = plik.read()

kody = re.findall(r'\d{2}-\d{3}', tekst)
print('kody pocztowe:', kody)

emaile = re.findall(wzorzec_emaila, tekst)
print('emaile:', emaile)

daty = re.findall(r'\d{1,2} [A-Z][a-z]{2} \d{4}', tekst)
print('daty:', daty)

