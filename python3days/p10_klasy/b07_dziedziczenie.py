class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def czy_jest_pelnoletnia(self):
        return self.wiek >= 18

    def __str__(self):
        return f'Osoba {self.imie} {self.nazwisko} ({self.wiek} lat)'

    def __repr__(self):
        return f'Osoba({repr(self.imie)}, {repr(self.nazwisko)}, {repr(self.wiek)})'

# Gdy mam już klasę Osoba i chcę utworzyć klasę, która będzie miała te same elementy, co Osoba,
# ale także coś więcej (lub coś ma w niej działać inaczej),
# to w tej sytuacji najlepiej utworzyć "podklasę" (subclass) klasy Osoba (która jest nadklasą (superclass)).
# Inaczej mówiąc klasa Student dziedzczy (inherits) z klasy Osoba, albo rozszerza (extends) klasę Osoba.
class Student(Osoba):
    # Jak w podklasie dodać nowe atrybuty?
    # Należy przedefiniować metodę init. W jej treści należy wywołać super().__init__, aby zainicjalzowąc obiekt na poziomie nadklasy

    def __init__(self, imie, nazwisko, wiek, rok, kierunek):
        super().__init__(imie, nazwisko, wiek)
        self.rok = rok
        self.kierunek = kierunek
        # W self można wprowadzić atrybut, któremu nie odpowiada żaden parametr.
        self.oceny = []

    # Jeśli chodzi o metody, top możliwe są takei sytuacje:

    # 1) W podklasie możemy dodać zupełnie nową metodę, której nie było w nadklasie
    # Przy okazji: pierwszy partametr metody, czyli "ten obiekt", nie musi nazywać się self
    # To tylko konwencja, a liczy się nie nazwa, tylko kolejność (pierwszy parametr)
    def dodaj_ocene(this, ocena):
        this.oceny.append(ocena)

    def srednia_ocen(self):
        if len(self.oceny) == 0:
            return None
        else:
            return sum(self.oceny) / len(self.oceny)

    # 2) Możemy też w ogóle nie mzieniaćistniejącej metody - wtedy w obiektach podklasy działa dokładnie ta sama metoda co w nadklasie
    # Tutaj przykładem jest czy_jest_pelnoletnia

    # 3) Metodę, która jest obecna w nadklasie, można w podklasie nadpisać (override).
    # Wtedy ta sama metoda wywoływana na obiektach nadklasy lub podklasy będzie działać w inny sposób.
    def przedstaw_sie(self):
        print(f'Hej, tu {self.imie}, studiuję na {self.rok} roku {self.kierunek}')


student = Student('Adam', 'Abacki', 23, 4, 'architektura')
print(student)

# Obiekt student posiada atrybuty i metody takie jak każda Osoba:
print(student.nazwisko)
print('pełnoletni?', student.czy_jest_pelnoletnia())

# Ale dodatkowo posiada atrybuty i metody dodane w podklasie:
print('kierunek studiów:', student.kierunek)
print('średnia ocen', student.srednia_ocen())
print()

if isinstance(student, Osoba):
    print('Student jest Osobą')
else:
    print('Student nie jest Osobą')

student.przedstaw_sie()

print()

# Polimorfizm i nadpisywanie metod


osoby = [
    Osoba('Ala', 'Kowalska', 30),
    Student('Adam', 'Abacki', 23, 3, 'biologia'),
    Osoba('Ola', 'Kowalska', 40),
    Osoba('Jan', 'Kowalski', 50),
    Student('Jola', 'Abacka', 23, 3, 'geografia'),
    Student('Andrzej', 'Andrzejski', 19, 1, 'medycyna'),
]

for ktos in osoby:
    # tutaj nie wiem czy "ktos" to Osoba czy Student. Ale wiem na pewno, że potrafi się przedstawić
    ktos.przedstaw_sie()
    # Obiekty zachowują się we właściwy dla siebie sposób, w zależności od tego jakiej są faktycznie klasy
