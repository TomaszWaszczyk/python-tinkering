print('Początek programu')
print('Otwieram plik...')

# Pliki otwiera się za pomocą open
# Domyślnie pliki są otwierane do odczytu, jako pliki tekstowe, w kodowaniu systemowym
# (na Linuxie lub Mac-u UTF-8, a na polskim Windowsie cp1250)
plik1 = open('plik.txt')
print('Plik otwarty:', plik1)

# Wczytanie całej zawartości pliku jako pojedynczej wartości str
# To jest dobre gdy:
# 1) tekst traktujemy jako jednolitą całość
# 2) plik nie jest zbyt duży
caly_tekst = plik1.read()

print('Cały tekst:')
print(caly_tekst)
print()

# Pliki należy zamykać - to zwalnia zasoby systemowe
# To ma większe znaczenie gdy:
# 1) zapsiujemy dane
# 2) lub gdy program ma działać dłużej i w swojej pracy wielokrotnie otwiera pliki
plik1.close()
print('Plik zamknięty:', plik1)
print()

# Jeśli chcemy mieć pełną kontrolę, to możemy podać parametry
# ścieżka, tryb (r - czytanie, w - pisanie), kodowanie znaków
plik2 = open('plik.txt', mode='r', encoding='UTF-8')

# readlines wczytuje całą zawartość pliku, ale jako listę stringów
# każda linia jako osobny string

# Ma to sens, gdy:
# 1) istotny jest podział tekstu na linie
# 2) chcemy mieć wszystkie linie wczytane do pamięci
#    - np. będziemy sortować dane
#    - albo będziemy wielokrotnie przeglądać te dane
# 3) plik nie jest zbyt duży

lista_linii = plik2.readlines()
print('W pliku było linii:', len(lista_linii))
print('Wszystkie linie:', lista_linii)
plik2.close()
print()

plik3 = open('plik.txt', mode='r', encoding='UTF-8')
# readline() - czyta jedną linię

pierwsza_linia = plik3.readline()
print('Pierwsza linia to:', pierwsza_linia)

druga_linia = plik3.readline()
print('Druga linia to:', druga_linia)

# wraz z czytaniem kolejnych fragmentów "kursor" w tym pliku przesuwa się na dalsze pozycje

# Za pomocą operacji seek można przenieść kursor na określoną pozycję
plik3.seek(0)
kolejna_linia = plik3.readline()
print('Po seek(0) kolejna linia:', kolejna_linia)

plik3.seek(4)
kolejna_linia = plik3.readline()
print('Po seek(4) kolejna linia:', kolejna_linia)
plik3.close()
print()


plik4 = open(file='plik.txt', mode='r', encoding='UTF-8')
# Używając readline() można też przejrzeć cały plik - w pętli

print('Pętla stosująca readline()')
while True:
    linia = plik4.readline()
    if not linia: break # to już koniec
    print(linia.strip())

plik4.close()
print()
# Ale ^takie^ przekombinowane podejście nie jest potrzebne, bo...


# Najbardziej typowy schemat w Pythonie
# Dzięki with plik "sam się zamknie", nie musimy jawnie pisać close()
# Plik tekstowy jest "iteratorem", dzięki czemu kolejne linie można czytać po prostu za pomocą for
with open('plik.txt', 'r', encoding='UTF-8') as plik5:
    for linia in plik5:
        print('Kolejna linia to:', linia)

print('Teraz plik5 jest zamknięty')

