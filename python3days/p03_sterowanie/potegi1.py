
# Program wypisuje w kolejnych liniach liczby z zakresu od 1 do 100 włącznie
# a obok tych liczby ich "kwadraty" (te liczby podniesione do potęgi 2).
# Można też do potęgi 3...

for i in range(1, 101):
#    print(i, i*i, i*i*i)
#    print(i, i**2, i**3)
#    print(f'{i} {i**2} {i**3}')
#    print(f'{i}\t{i**2}\t{i**3}')
    print(f'{i:4}{i**2:8}{i**3:10}')

