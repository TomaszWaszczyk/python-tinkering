class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def czy_jest_pelnoletnia(self):
        return self.wiek >= 18

    # Metoda specjalna str ma zwracać (return) tekstową reprezentację obiektu
    # To co zwróci str zostanie użyte podczas wypisywania obiektu za pomocą print,
    # podczas konwersji na tekst za pomocą str(obiekt) itp.
    def __str__(self):
        return f'Osoba {self.imie} {self.nazwisko} ({self.wiek} lat)'

    # repr zwraca techniczną postać obiektu
    # to ma być fragment kodu Pythona, który spowoduje utworzenie takiego samego obiektu
    def __repr__(self):
        return f'Osoba({repr(self.imie)}, {repr(self.nazwisko)}, {repr(self.wiek)})'


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

    def __str__(self):
        return f'Kurs języka {self.jezyk}'


a = Osoba('Ala', 'Kowalska', 30)
b = Osoba('Ola', 'Malinowska', 15)

print('Efekt wypisania obiektów:')
print(a)
print(b)

a_tekstowo = str(a) # równoważne a.__str()__
print(a_tekstowo)
print()

print('Wyniki repr')
print(repr(a))
print(repr(b))

print('\nEfekt wywołania przedstaw_sie():')
a.przedstaw_sie()
b.przedstaw_sie()

print('Odczyt pojedynczej informacji:', b.imie)
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

