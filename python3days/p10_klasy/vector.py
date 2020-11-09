class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # @property oznacza, że wynik tej metody będzie się odczytywać tak jakby to był atrybut (zmienna obiektu)
    # czyli bez nawiasów
    # np. v.length a nie v.length()
    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'<{self.x},{self.y}>'

    def __repr__(self):
        return f'Vector({repr(self.x)},{self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number)

    def __rmul__(self, number):
        return Vector(self.x * number, self.y * number)

    # dzielenie przez liczbę. truediv to jest /  , floordiv to // ,
    def __truediv__(self, number):
        return Vector(self.x / number, self.y / number)

    # Czy wektory tej samej długości, ale w innym kierunku mają być sobie równe?
    # 3,4  == 4,3  ??? To decyzja projektowa.
    # Chociaż matematycznie to nie jest prawda, to tu przyjmijmy że tak - że we wszystkich porównaniach bierzemy pod uwage długość wektora

    # def __eq__(self, other):
    #     return self.x == other.x and self.y == other.y

    def __eq__(self, other):
        return self.length == other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __bool__(self):
        return self.x != 0 or self.y != 0
        # zwracamy True jeśli wektor jest niezerowej długości


a = Vector(3, 4)
b = Vector(x=2, y=1)

print(a)
print(b)
print(repr(b))
c = a + b
print(c, type(c))
print(c - a)
print()
# Gdyby drugim argumentem nie był Vector, to będzie błąd
# print(a - 5)

print(a)
d = a * -3
print(d, type(d))

e = 5 * a
print(e, type(e))
print()

print("długość a:", a.length)
print("długość b:", b.length)
b.y = 1.5
print("długość b:", b.length)

print(a == b) # wywołanie metody eq, to odpowiada equals w Javie
print(a is b) # sprawdzenie tożsamości obiektu (mówiąv techniczne: adresów) - "czy to ten sam obiekt" - odpowiednik == w Javie i === w PHP
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

if a > b:
    print('wektor a jest dłuższy')
else:
    print('b')

if a:
    print('Wektor nie jest zerem')
