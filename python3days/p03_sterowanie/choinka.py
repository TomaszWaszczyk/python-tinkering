wysokosc = int(input('Podaj wysokość choinki: '))

for w in range(wysokosc):
    print(' ' * (wysokosc-w), '*' * (2*w+1))
