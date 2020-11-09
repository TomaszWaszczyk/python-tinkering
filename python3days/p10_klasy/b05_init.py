# Dopiero ta wersja definicji klasy jest godna naśladowania.

# Klasa jest kontrukcją, wewnątrz której można definiować funkcje.
# Funkcje definiowane wewnątrz klas nazywają się "metody".
# Potem tworzy się obiekty danej klasy, a w obiektach mogą być przechowywane atrybuty.

class Osoba:
    # __init__ jest specjalną metodą, która jest wykonywama w momencie tworzenia obiektu
    # Jej rolą jest takie przygotowanie obiektu (czyli self-a), aby był on gotowy do pracy
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def czy_jest_pelnoletnia(self):
        return self.wiek >= 18


class Kurs:
    def __init__(self, jezyk, miasto, czas_trwania, program):
        self.jezyk = jezyk
        self.miasto = miasto
        self.czas_trwania = czas_trwania
        self.program = program

    def wypisz_zaproszenie(self):
        kwota = self.czas_trwania * 400
        print(f'Zapraszamy na kurs języka {self.jezyk} w {self.miasto}.')
        print(f'W {self.czas_trwania} dni nauczysz się wszystkiego za jedyne {kwota}.')

    def wypisz_program(self):
        print(f'Kurs języka {self.jezyk} obejmuje następujące tematy:')
        for punkt in self.program:
            print(f' * {punkt}')


a = Osoba('Ala', 'Kowalska', 30)
b = Osoba('Ola', 'Malinowska', 15)

# Gdy tworzymy obiekt pisząc
# c = Osoba('Ela', 'Nowakowska', 35)
# Python robi coś takiego:
c = Osoba.__new__(Osoba)
c.__init__('Ela', 'Nowakowska', 35)


print('Efekt wypisania obiektów:')
print(a)
print(b)
print(c)

print('\nEfekt wywołania przedstaw_sie():')
a.przedstaw_sie()
b.przedstaw_sie()
c.przedstaw_sie()
print()

# Teraz tworząc obiekt Osoba MUSIMY przekazać wszystkie wymagane parametry init
# c = Osoba()

for o in [a, b]:
    if o.czy_jest_pelnoletnia():
        print(o.imie, 'jest pełnoletnia')
    else:
        print(o.imie, 'jest niepełnoletnia')
print()


kurs1 = Kurs('Python', 'Warszawa', 10,
             ['zmienne', 'pętle', 'listy', 'klasy', 'Pandas', 'Django'])

kurs2 = Kurs('Java', 'Katowice', 8,
            ['typy', 'pętle', 'tablice', 'klasy', 'Spring', 'Hibernate'])

kurs1.wypisz_zaproszenie()
kurs1.wypisz_program()
print()

kurs2.wypisz_zaproszenie()
kurs2.wypisz_program()

