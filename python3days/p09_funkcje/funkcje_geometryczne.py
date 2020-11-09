import math

def pole_kwadratu(a):
    return a * a

def pole_kola(r):
    return math.pi * r * r

def pole_prostokata(a, b):
    return a * b

def obwod_prostokata(a, b):
    return 2 * a + 2 * b


liczba1 = float(input('Podaj pierwszą liczbę: '))
liczba2 = float(input('Podaj drugą liczbę: '))
print('Pole kwadratu:', pole_kwadratu(liczba1))
print('Pole koła:', pole_kola(liczba1))
print('Pole prostokąta:', pole_prostokata(liczba1, liczba2))
print('Obwód prostokąta:', obwod_prostokata(liczba1, liczba2))
