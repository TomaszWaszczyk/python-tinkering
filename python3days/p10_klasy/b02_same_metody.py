# Klasa jest kontrukcją, wewnątrz której można definiować funkcje.
# Funkcje definiowane wewnątrz klas nazywają się "metody".
class Osoba:
    def przedstaw_sie(self):
        print('Jestem osobą')

    def czy_jest_pelnoletnia(self):
        return True


# Mając zdefiniowane klasy w działającym, programie możemy
# tworzyć obiekty tych klas
ktos = Osoba()

# A na obiekcie możemy wywołać metodę:
ktos.przedstaw_sie()
print()


class Kurs:
    def wypisz_zaproszenie(self):
        print('Zapraszamy na kurs programowania')

    def wypisz_program(self):
        print('Fejkowy program kursu...')

kurs_pythona = Kurs()
kurs_pythona.wypisz_zaproszenie()
kurs_pythona.wypisz_program()
print()

kurs_javy = Kurs()
kurs_javy.wypisz_zaproszenie()
kurs_javy.wypisz_program()
