# Wypisz 100 kolejnych potęg liczby 2:  1 2 4 8 16 32 64 ...

# Sposób 1
for i in range(100):
    print(i, 2**i)

print()

# Sposób 2
x = 1
while x < 10**100:
    print(x)
    x *= 2
