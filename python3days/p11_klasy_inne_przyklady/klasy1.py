'''
Programowanie obiektowe to taki styl ("paradygmat") programowania, w którym działająca aplikacja składa się
z "obiektów", które przechowują stan, wykonują różne czynności, "komunikują się" wywołując metody.
'''

# Przykład: pamiętajmy dane jakichś osób.
# Podejście do programowania bez obiektów:
imie = 'Ala'
nazwisko = 'Kowalska'
wiek = 30

# Problemy: nie widać, że te dane są ze sobą powiązane; że są to dane tej samej osoby.
# Gdybym chciał dane osoby przekazać do jakiejś funkcji, to musiałbym prekazywać wiele parametrów

def sprzedaj_piwo_v1(imie, wiek):
    if wiek >= 18:
        print(f'{imie} może kupić piwo')
    else:
        print(f'{imie} nie może kupić piwa, bo ma tylko {wiek} lat.')

def przedstaw_osobe(imie, nazwisko, wiek):
    print(f'Osoba nazywa się {imie} {nazwisko} i ma {wiek} lat.')

sprzedaj_piwo_v1(imie, wiek)

imie2 = 'Ola'
nazwisko2 = 'Malinowska'
wiek2 = 15
sprzedaj_piwo_v1(imie2, wiek2)
print()

# Za pomocą klas i obiektów możemy takie rzeczy realizować porządniej,
# w sposób bardziej zorganizowany i czytelny.

# To będzie "obiektowy styl programowania"

 # Klasa jest "wzorcem" dla obiektów. Programista definiuje klasę, a w czasie działania programu tworzone są obiekty ("instancje") tej klasy.
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstawSie(self):
        print(f'Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')


class Sklep:
    def __init__(self):
        self.ilosc_sprzedanych_piw = 0

    def sprzedaj_piwo(self, osoba):
        if osoba.wiek >= 18:
            print(f'{osoba.imie} może kupić piwo')
            self.ilosc_sprzedanych_piw += 1
        else:
            print(f'{osoba.imie} nie może kupić piwa, bo ma tylko {osoba.wiek} lat.')


# Teraz tworzę obiekty
ala = Osoba('Ala', 'Kowalska', 30)
ola = Osoba('Ola', 'Malinowska', 15)

# Obiekt posiada pewne dane ("stan") - to są jego "atrybuty"
print(ala.imie, ala.wiek)

# Obiekt charakteryzuje się też jakimś "zachowaniem".
# To zachowanie jest określone przez metody, które można na obiekcie wywołać.
# Inaczej mówiąc: obiekt potrafi wykonać pewne czynności.
ala.przedstawSie()
ola.przedstawSie()
print()

sklep = Sklep()
sklep.sprzedaj_piwo(ala)
sklep.sprzedaj_piwo(ola)

print('Sklep sprzedał w sumie piw:', sklep.ilosc_sprzedanych_piw)
