# Specyfika list:
# listy mogą zawierać duplikaty
# kolejność jest zachowywana
# można indeksować (lista[i], wycinanki...)
# listy są "mutowalne" (mutable) - można zmieniać zawartość listy

# pusta lista na dwa sposoby:
pusta_lista_1 = []
pusta_lista_2 = list()
print(pusta_lista_1, type(pusta_lista_1))
print(pusta_lista_2, type(pusta_lista_2))
print()


lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań']
print(lista)

# len - rozmiar kolekcji, liczba elementów
print(' len:', len(lista))

# de facto to jest wywołanie takiej metody, ale "zwykły programista" powinien używać funkcji len() aby to uzyskać
print('_len:', lista.__len__())


# pętla for pozwala przejrzeć zawartość kolekcji i zrobić coś dkla każdego elementu:
for miasto in lista:
    print(' * ', miasto)
print()

# Operator in sprawdza czy element należy do kolekcji
# Takie rzeczy jak in, index dla list są kosztowne - wymagają przejrzenia całej listy (aż do znalezienia elementu albo do samego końca)
if 'Wrocław' in lista:
    indeks = lista.index('Wrocław')
    # opcjonalne parametry start i stop
    print('Wrocław jest na liście, a jego pozycją jest', indeks)
else:
    print('Wrocławia nie ma liście')
print()

if 'Radom' in lista:
    print('Radom jest')
else:
    print('Radomia nie ma')
print()

# dostęp do pojedynczego elementu listy:  lista[indeks]
# numeracja od zera
print(lista[0], lista[3])

print(lista)

# zmiana wartości jednego elementu (nadpisanie):
lista[0] = 'Wawa'
print(lista)

# dodanie elementu na koniec listy:
lista.append("Szczecin")
print(lista)

# extend - dodanie wielu elementów (całej kolekcji) na końcu
dodatkowe = ['Bydgoszcz', 'Toruń']
lista.extend(dodatkowe)
print(dodatkowe)
print(lista)

# usunięcie elementu z listy - lista się "zapada" - długość ulego zmniejszeniu
del lista[0]
print(lista)

# wstawienie elementu na określoną pozycję - elementy na prawo od tej pozycji są przesuwane
lista.insert(0, 'Warszawa')
print(lista)

# do wstawiania elementów można też użyć zakresów:
# O "wycinankach" jest inny przykład
lista[5:5] = ['Trójmiasto']
print(lista)

print(lista[5:6]) # ['Trójmiasto']
# zastąp wycinek o długości jeden tymi trzema elementami
# zastępuje Trójmiasto tymi trzema miastami
lista[5:6] = ['Gdańsk', 'Sopot', 'Gdynia']
# trzy_miasta = ['Gdańsk', 'Sopot', 'Gdynia']
# lista[5:6] = trzy_miasta
print(lista)

# lista[3:6] = []
# print(lista)

# usuwanie podanej wartości - pierwsze wystąpienie, a gdy nie znajdzie, to błąd
lista.remove('Wrocław')
print(lista)

# Listy można dodawać. Nie wpływa to na istniejące obiekty, tylko tworzy w wyniku nowy.
dodatkowe = ['Berlin', 'Praga', 'Moskwa']
nowa_lista = lista + dodatkowe
print(nowa_lista)
print(lista)
print()

# Można nawet mnożyć listę przez liczbę całkowitą - oznacza to powielenie wartości
print(10 * lista)
nowa_lista = lista + 2*dodatkowe
print(nowa_lista)
print()

# Ze względu na sposób, w jaki listy są w Pythonie zaimplementowane,
# dodawanie na koniec, usuwanie z końca - działają szybko
# dodawanie i usuwanie na początku bądź w środku listy jest wolne, podobnie jak sprawdzanie czy element należy do listy.
print()

# tupla, krotka
tupla = ('Ala', 'Ola', 'Ela')
print(tupla)


# tuple mogą zawierać duplikaty
# kolejność jest zachowywana
# można indeksować (lista[i], wycinanki...)
# tuple są "niemutowalne" (immutable)
print(tupla[1])
print(tupla[0:2])

# nie zadziałają:
# tupla[1] = 'Aleksandra'
# TypeError: 'tuple' object does not support item assignment
# tupla[2:3] = ('Ela', 'Ula')

# tupla.append('Ula')
# tupla.insert(2, 'Ewa')
# del tupla[1]

# pusta tupla:
pusta_tupla_1 = ()
pusta_tupla_2 = tuple()
print(pusta_tupla_1, type(pusta_tupla_1))
print(pusta_tupla_2, type(pusta_tupla_2))

# jak utworzyć tuplę jednoelementową?
# nie tak:
tupla1 = (123)
print(tupla1, type(tupla1))

# tylko tak:
tupla1 = (123,)
print(tupla1, type(tupla1))
print()

# ZASTOSOWANIA
# "Normalny programista Pythona" zdecydowanie częściej używa list
# tuple są intensywnie używane wewnętrznie przez Pythona - m.in. przekazywanie parametrów do funkcji
# tuple są używane przy realizacji różnych Pythonowych sztuczek, np. przeglądanie zawartości słowników
# przy "rozpakowywaniu", zwracaniu wielu wyników na raz itp.

# Przykład zwracania dwóch wyników na raz i ich rozpakowania
def dzielenie_z_reszta(x, y):
    return x//y, x%y

tupla_wynikowa = dzielenie_z_reszta(20, 7)
print('typ wyniku:', type(tupla_wynikowa))

# "rozpakowywanie"
(iloraz, reszta) = tupla_wynikowa
print(f'Wynik dzielnia to {iloraz} i {reszta} reszty')

# Ja (Patryk) w takich sytuacjach piszę te okrągłe nawiasy,
# ale składnia Pythona w wielu sytuacjach pozwala nie pisać tych niawiasów, tylko sam przecinek
a, b = dzielenie_z_reszta(20, 7)

# W typowym zastosowaniu lista zawiera wiele jendorodnych elementów (np. same napisy, albo same liczby)
# nieograniczonej długości. Typowe jest, że do list są dodawane nowe elemente w czasie działania programu.
imiona = ['Ala', 'Ola', 'Ela']
imiona.append('Ula')
print(imiona)

# Tuple natomiast często zawierają dane różnych typów lub kolejne pola pełnią różną rolę.
# Zwykle tuple mają z góry znany rozmiar i wiadomo co będzie na której pozycji
# (jak w rekordzie bazodanowym)
t2 = ('Ala', 'Kowalska', 30, 'Jasna', 'Warszawa', True)
print(t2)

# Python tego nie sprawdza, ale taka jest praktyka użycia...

# Rada: gdy nie wiemy czego użyć, użyjmy listy.

