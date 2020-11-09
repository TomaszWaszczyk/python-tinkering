# Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
# Sprawdź jak dużo z tych liczb jest liczbami parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu zbiorów.

# Można przyjąć, że user przestaje wprowadzać dane, gdy wpisze pusty string

# input   int   range   set     &

liczby = set()
while True:
    s = input('Podaj liczbę: ')
    if not s: break
    try:
        liczby.add(int(s))
    except ValueError:
        print('To nie jest liczba')

print('Wprowadzone liczby:', liczby)
print('Jest ich', len(liczby))

parzyste = liczby & set(range(0, 101, 2))
print('W tym parzystych z zakresu:', len(parzyste))
print('Czyli:', parzyste)
