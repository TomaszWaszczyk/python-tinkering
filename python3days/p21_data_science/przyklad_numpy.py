import numpy

a = numpy.arange(10)
b = numpy.arange(100, 200, 5)

print(a)
print(b)

print(b[2:5])

print(sum(a))

print(sum(b[2:5]))

m = numpy.array([[ 1,  2,  3,  4,  5],
                 [20, 30, 40, 50, 60],
                 [ 0,  1,  2,  1,  0]])

n = numpy.arange(3)

print(m)
print(n)
print()

print(n @ m)
