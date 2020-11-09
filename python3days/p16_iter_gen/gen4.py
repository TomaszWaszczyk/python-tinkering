def fib(count=1000):
    n = 0
    (a, b) = (0, 1)
    while n < count:
        yield a
        (a, b) = (a + b, a)
        n += 1


for x in fib(1000):
    print(x)

