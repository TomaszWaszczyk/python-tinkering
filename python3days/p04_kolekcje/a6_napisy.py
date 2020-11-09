# Napisy (czyli str) w Pythonie jest sekwencją znaków.
# Można iterować za pomocą pętli for,
# można wycinać fragmenty.
# Stringi są niemutowalne.

napis = 'Ala ma kota'
print(len(napis))

for znak in napis:
	print('Kolejny znak:', znak)
print()

print('Typ napisu:', type(napis))
print('Typ znaku:', type(napis[4]))

print(napis[4])
print(napis[4:6])
# Zawartości napisu nie da się zmienić, to nie są tablice takie jak w C. str is immutable
# napis[7] = 'K'
print()

if 'm' in napis:
	print('Jest literka m')
else:
	print('Nie ma literki m')

# Dla napisów operator in sprawdza czy napis jest fragmentem dużego napisu (a nie tylko czy litera jest elementem)
if 'kot' in napis:
	print('kot obecny')
else:
	print('nie ma kota')

print('kot jest na pozycji', napis.index('kot'))
print('kot jest na pozycji', napis.find('kot'))
# Gdy nie znajdą: index wyrzuca wyjątek, a find zwraca -1
print()

# Napisy można dodawać - wynikiem jest nowy napis
nowy = napis + ' oraz psa'
print('nowy napis:', nowy)
print('stary napis:', napis)

# Napisy można mnożyć przez liczbę całkowitą - oznacza powtózenie treści
print('Ala ma kota. ' * 10)

print()

########

# W Pythonie napisy można podawać w "cudzysłowach" albo w 'apostrofach'
napis = "Ola ma psa"
print(type(napis))
print(napis)
print()

# Napis rozciągający na wiele linii można wpisać za pomocą
# potrójnych znaczków ''' lub """
# Często używa się tego jako komentarzy lub dokumentacji (docstring), ale jest to także normalny napis.

tekst = '''Litwo, ojczyzno moja
ty jesteś jak zdrowie'''

print(type(tekst))
print(tekst)

def funkcja(a,b):
	'''
	Funkcja dodaje dwie liczby
	:param a: pierwsza liczba
	:param b: druga liczba
	:return: suma liczb a i b
	'''
	return a + b


wynik = funkcja(5, 10)

# Jesli chcemy mieć tekst w jednej linii, ale w kodzie programu go podzielić,
# to w ten sposób:
tekst = 'Ala ma kota, ' \
	+ 'a Ola ma psa.'

tekst = ('Ala ma kota, '
		'a Ola ma psa ' 'i chomika')

print(tekst)
print()

# W niektórych sytuacjach w Pythonie używa się specjalnych wersji napisu z magiczną literą na początku.

# f-string - do wklejania i formatowania wartości
ile = 7
print(f'Ala ma {ile} kotów')
print()

# raw-string - aby znaki specjalne nie były przetwarzane.
# Najczęstsze zastosowania: wyrażenia regularne, ścieżki do plików.

# np. w normalnym napisie \t zamienia się w tabulator, \n w znak nowej linii,
# \" i \' w cudzysłów i apostrof, a \\ oznacza pojedynczy \
zwykly = 'Ala\tma\tkota \'Filemona\'\nOla\tma\tpsa\\ \"Burka\"\n'
print('zwykły', type(zwykly), len(zwykly))
print(zwykly)
print()

print('Natmomiast te backslashe się wypiszą: \w\s')

# W surowym stringu (raw-string) te specjalne ciągi są traktowane jak normalna zawartość stringa.
surowy = r'Ala\tma\tkota \'Filemona\'\nOla\tma\tpsa\\ \"Burka\"'
print('surowy', type(surowy), len(surowy))
print(surowy)
print()

# Zastosowania: ścieżki do plików, wyrażenia regularne

# W Pythonie 2 napisy Unicodowe należało wpisywać w u-stringi
# u'Zażółć gęślą jaźń'
