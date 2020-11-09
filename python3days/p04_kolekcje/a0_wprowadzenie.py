# Zamiast pamiętać różne wartości na różnych zmiennych

imie1 = 'Ala'
imie2 = 'Ola'
imie3 = 'Ela'
print(imie1, imie2, imie3)

# Można użyć kolekcji, w tym przyoadku listy:

imiona = ['Ala', 'Ola', 'Ela']
print(imiona[0], imiona[1], imiona[2])
print(imiona)

for imie in imiona:
    print(imie, end='; ')
print()
print()

# Podstawowe rodzaje kolekcji:

# lista
lista = [10, 11, 12, 13, 14]
print(lista)
lista.append(15)
print(lista[2]) # 12
lista[2] += 100
print(lista[2]) # 112
print()

# tupla
tupla = (10, 11, 12, 13, 14)
print(tupla)
print(tupla[2])
# para = (3, 4)
# wspolrzedne = (x, y, z)
print()

# zbiór (set)
# nie ma powtórzeń
zbior = {10, 11, 12, 10, 14, 11}
print(zbior)
zbior.add(20)
zbior.add(12)
print(zbior)
print()

# słownik (dict)
# dla klucza pamiętamy wartość, klucze muszą być unikalne
slownik = {'Ala': 20, 'Ola': 30}
slownik['Ela'] = 40
print(slownik)
imie = 'Ola'
print(slownik[imie])

for osoba, wiek in slownik.items():
    print(f'{osoba} ma {wiek} lat')
