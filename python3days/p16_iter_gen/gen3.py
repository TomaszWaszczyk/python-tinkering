def nieparzyste(limit=1_000_000):
    n = 1
    while n < limit:
        yield n
        n += 2


for x in nieparzyste(100):
    print(x)


