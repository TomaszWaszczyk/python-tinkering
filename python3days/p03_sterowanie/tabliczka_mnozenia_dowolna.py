n = int(input('Podaj wielkość tabliczki: '))
s = len(str(n*n))

for w in range(1, n+1):
    for k in range(1, n+1):
        print(f'{w*k:{s}} ', end='')
    print()
