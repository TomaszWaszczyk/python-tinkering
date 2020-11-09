# Wypisz na ekran tabliczkę mnożenia 10x10

for w in range(1, 11):
    for k in range(1, 11):
        print(f'{w*k:3} ', end='')
    print()
