# "Type hints" to są "nieformalne" informacje o typach zmiennych.
# To jest forma dokumentacji i podpowiedzi dla narzędzi deweloperskich, np. PyCharm,
# Interpreter Pythona nie bierze tego pod uwagę.

napis:str = 'Ala ma kota'
liczba:int = 1234

print(napis, liczba)

# Nie będzie błędem wpisanie danych innego typu.

napis = 333
liczba = [3.14, 4.55]

print(napis, liczba)
