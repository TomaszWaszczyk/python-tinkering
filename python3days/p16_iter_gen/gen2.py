def nieparzyste():
    n = 1
    while True:
        yield n
        n += 2


for x in nieparzyste():
    print(x)


