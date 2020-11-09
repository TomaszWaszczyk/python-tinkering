# Typowa klasa w Pythonie nie ma zmiennych definiowanych na poziomie klasy (czasami ma, ale o tym później....)
# natomiast zawiera definicje metod.
# Metoda __init__ ma specjalne znaczenie, pełni rolę konstrukora.
# Atrybuty obiektu (czyli "zmienne trzymane w obiekcie") określa się wewnątrz metody init.
# W każdym miejscu, gdzie odwołuję się do atrybutów, muszę pisać self.
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstawSie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

    def pelnoletnia(self):
        if self.wiek >= 18:
            return True
        else:
            return False

    @staticmethod
    def statyczna():
        print('Jestem metodą statyczną')


# końcem definicji klasy jest po prostu koniec wciętego bloku

a = Osoba('Ala', 'Kowalska', 30)
print(a)

b = Osoba('Ola', 'Malinowska', 35)
print(b)
print()

a.przedstawSie()
b.przedstawSie()
print()

print('Atrybuty obiektu a:', a.imie, a.nazwisko, a.wiek)
a.wiek += 1
print('Atrybuty obiektu a:', a.imie, a.nazwisko, a.wiek)
a.przedstawSie()
print('Ala pełnoletnia?', a.pelnoletnia())
print()
