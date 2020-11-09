
print('Kawałek tekstu')
print(2+2*3)
# W Pythonie nie wolno odczytywać  niezdefiniowanych zmiennych - błąd w czasie działania
# print(zmienna)

# Aby zdefiniować zmienną, po prostu przypisujemy wartość do zmiennej
zmienna = 123
print(zmienna)

# Wartość zmiennej można zmienić
zmienna = 200
print(zmienna)
zmienna += 10
print(zmienna)

print('Typ:', type(zmienna))

# W Pythonie zmienna NIE MA TYPU.
# W zmiennej jest zapisana jakaś wartość, i to wartość jest jakiegoś typu
# W praktyce oznacza to tyle, że na każdą zmienną w dowolnym momencie można wpisać wartość dowolnego typu:

zmienna = 'Ala ma kota'
print(zmienna)
print('Typ:', type(zmienna))
