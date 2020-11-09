# Klasa jest kontrukcją, wewnątrz której można definiować funkcje.
# Funkcje definiowane wewnątrz klas nazywają się "metody".
class Osoba:
    def przedstaw_sie(self):
        # Zakładając, że obiekt posiada już atrybutry imie, nazwisko, wiek
        # Odczytujemy je z selfa
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def czy_jest_pelnoletnia(self):
        return self.wiek >= 18


class Kurs:
    def wypisz_zaproszenie(self):
        kwota = self.czas_trwania * 400
        print(f'Zapraszamy na kurs języka {self.jezyk} w {self.miasto}.')
        print(f'W {self.czas_trwania} dni nauczysz się wszystkiego za jedyne {kwota}.')

    def wypisz_program(self):
        print(f'Kurs języka {self.jezyk} obejmuje nasatępujące tematy:')
        for punkt in self.program:
            print(f' * {punkt}')


# Mają zdefiniowane klasy w działającym, programie możemy
# tworzyć obiekty tych klas
a = Osoba()

# Gdyby teraz wywołał metodę przedstaw_sie, gdy atrybuty imie nazwisko nie są ustawione,
# Doszłoby do błędu AttributeError
# a.przedstaw_sie()

# W obiektach można zapisywać swego rodzaju zmienne, na które mówi się:
# atrybut (attribute), pole (field)
a.imie = 'Ala'
a.nazwisko = 'Kowalska'
a.wiek = 30

# Teraz na obiekcie możemy wywołać metodę.
a.przedstaw_sie()

# Gdy wywołuję metodę na konkretnym obiekcie,
# to ten obiekt (w tym przypadku a) staje się parametrem self.
# Tak jakby wywołać normalną funkjcę pisząc:  przedstaw_sie(a)
# Zadziała nawet coś takiego, ale to nie jest normalne podejście:
Osoba.przedstaw_sie(a)


# Można tworzyć wiele obiektów tej samej klasy
b = Osoba()
b.imie = 'Ola'
b.nazwisko = 'Malinowska'
b.wiek = 15
b.przedstaw_sie()

for o in [a, b]:
    if o.czy_jest_pelnoletnia():
        print(o.imie, 'jest pełnoletnia')
    else:
        print(o.imie, 'jest niepełnoletnia')


print()

kurs1 = Kurs()
kurs1.jezyk = 'Python'
kurs1.miasto = 'Warszawa'
kurs1.czas_trwania = 10
kurs1.program = ['zmienne', 'pętle', 'listy', 'klasy', 'Pandas', 'Django']

kurs2 = Kurs()
kurs2.jezyk ='Java'
kurs2.miasto = 'Katowice'
kurs2.czas_trwania = 8
kurs2.program = ['typy', 'pętle', 'tablice', 'klasy', 'Spring', 'Hibernate']

kurs1.wypisz_zaproszenie()
kurs1.wypisz_program()
print()

kurs2.wypisz_zaproszenie()
kurs2.wypisz_program()


