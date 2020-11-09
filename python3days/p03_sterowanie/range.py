# Jedną z możliwości pobierania elementów, jest ich generowanie za pomocą range.
# range generuje kolejne liczby całkowite z jakieś przedziału
# Jest kilka możliwości użycia:

# range(koniec) - wygeneruje liczby od 0 włącznie do koniec wyłączając
print("\n=========")
print("range(10):")
for i in range(10):
   print(i)

print("\n=========")
print("range(10, 20):")
# range(poczatek, koniec) - wygeneruje liczby od poczatek włącznie do koniec wyłączając
# w tym przypadku od 10 do 19
for liczba in range(10, 20):
   print(liczba)

print("\n=========")
print("range(10, 24, 3):")
# range(poczatek, koniec, krok) - wygeneruje liczby od początek włącznie do koniec wyłączając,
# generując kolejne z podanym krokiem
# w tym przypadku: 10, 13, 16, 19, 22,
for liczba in range(10, 24, 3):
   print(liczba)
print()

print("range(100, 50, -5):")
for liczba in range(100, 50, -5):
   print(liczba)
print()

# Argumentami range mogą być wartości zmiennych i innych wyrażeń
start = 40
stop = 60
step = 5
for x in range(start, stop, step):
   print(x)
print()

# Jeśli parametry są ułożone tak, że warunek od początku jest fałszywy, to range nic nie wygeneruje, a pętla się nie wykona (ale nie ma błędu)
for y in range(50, 30):
   print('y:', y)
print()

# range to nie jest kolekcja wszystkich tych liczb, tylko to jest generator, który potrafi je wygenerować
maszynka = range(1000_000_000)
print(maszynka)
# for i in maszynka:
#     print(i)

