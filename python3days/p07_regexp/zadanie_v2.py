import re

# W tej wersji wstepnie kompiluję wzorce. Dopóki nie ma pętli to i tak nie zmienia wydajności...

wzorzec_kodu = re.compile(r'\d{2}-\d{3}')
wzorzec_emaila = re.compile(r'[A-Za-z0-9_.\-]+@(?:[A-Za-z0-9_\-]+\.)+[A-Za-z]+')
wzorzec_daty = re.compile(r'\d{1,2} [A-Z][a-z]{2} \d{4}')

with open('re_teksty.txt') as plik:
    tekst = plik.read()

kody = re.findall(wzorzec_kodu, tekst)
print('kody pocztowe:', kody)

emaile = re.findall(wzorzec_emaila, tekst)
print('emaile:', emaile)

daty = re.findall(wzorzec_daty, tekst)
print('daty:', daty)

