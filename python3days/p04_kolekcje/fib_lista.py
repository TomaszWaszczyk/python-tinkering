# Napisz program, który prosi o podanie liczby N, a następnie buduje listę N pierwszych liczb Fibonacciego
# Liczby Fibonacciego są zdefiniowane tak:
# F(0) = 0, F(1) = 1, a następnie F(x) = F(x-2) + F(x-1)
# Czyli kolejna liczba F. jest sumą dwóch poprzednich, początek ciągu to:
# 0 1 1 2 3 5 8 13 21 34 55

limit = int(input('Podaj limit: '))

f = [0, 1]
for i in range(2, limit+1):
    f.append(f[-1] + f[-2])

# print(f)

# enumerate generuje pary (index, value), można to rozpakować i łatwo pisać pętle for z licznikiem i wartością
for indeks, liczba in enumerate(f):
    print(f'{indeks:5} → {liczba}')


# for liczba in f:
#     print(f'???? → {liczba}')

