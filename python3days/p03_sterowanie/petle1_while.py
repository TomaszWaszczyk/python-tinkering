# W Pythonie są 2 rodzaje pętli: while , for

# while WARUNEK:
#    TREŚĆ

x = 1
while x <= 10:
    print('x jeszcze się mieści, bo ma wartość', x)
    x += 1

print('Pętla się zakończyła, teraz x = ', x)
print()

y = 1000
while y > 1:
    print(y)
    y /= 2
print()

# W Pythonie pętle mogą mieć else - wyjaśnienie w innym pliku
x = 100
while x < 110:
    print(x)
    x = x+1
else:
    print('ELSE', x)

print('Koniec')
